
from flask import render_template, request, url_for, redirect, current_app
from app import app, db
from models import Torcedor

@app.route('/')
def index():
    torcedores = Torcedor.query.all()
    return render_template("index.html", torcedores=torcedores)

@app.route('/adicionar',methods=['GET','POST'])
def adicionar():
    if request.method == 'POST':
        if cpf_validate(request.form['cpf']):
            try:
                torcedor = Torcedor(request.form['nome'], request.form['data_de_nascimento'],request.form['time'].lower(), request.form['email'], request.form['cpf'])
                db.session.add(torcedor)
                db.session.commit()
                return redirect(url_for('index'))
            except:
                db.session.rollback()
                erro = 1
                return render_template('adicionar.html',erro=erro)
        else:
            erro = 2
            return render_template('adicionar.html', erro=erro)
    if request.method == 'GET':
        return render_template('adicionar.html')

@app.route('/deletar/<int:id>')
def deletar(id):
    torcedor = Torcedor.query.get(id)
    db.session.delete(torcedor)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/editar/<int:id>', methods=['GET','POST'])
def editar(id):
    torcedor = Torcedor.query.get(id)
    if request.method == 'POST':
        if cpf_validate(request.form['cpf']):
            try:
                torcedor.nome = request.form['nome']
                torcedor.data_nascimento = request.form['data_de_nascimento']
                torcedor.time = request.form['time'].lower()
                torcedor.email = request.form['email']
                torcedor.cpf = request.form['cpf']
                db.session.commit()
                return redirect(url_for('index'))
            except:
                db.session.rollback()
                erro = 1
                return render_template('adicionar.html', erro=erro)
        else:
            erro = 2
            return render_template('adicionar.html', erro=erro)
    if request.method == 'GET':
        return render_template('editar.html',torcedor=torcedor)


def cpf_validate(numbers):
    #  Obtém os números do CPF e ignora outros caracteres
    cpf = [int(char) for char in numbers if char.isdigit()]

    #  Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    #  Verifica se o CPF tem todos os números iguais, ex: 111.111.111-11
    #  Esses CPFs são considerados inválidos mas passam na validação dos dígitos
    #  Antigo código para referência: if all(cpf[i] == cpf[i+1] for i in range (0, len(cpf)-1))
    if cpf == cpf[::-1]:
        return False

    #  Valida os dois dígitos verificadores
    for i in range(9, 11):
        value = sum((cpf[num] * ((i + 1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return False
    return True