
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
        torcedor = Torcedor(request.form['nome'], request.form['data_de_nascimento'],request.form['time'], request.form['email'], request.form['cpf'])
        db.session.add(torcedor)
        db.session.commit()
        return redirect(url_for('index'))
    if request.method == 'GET':
        return render_template('adicionar.html')