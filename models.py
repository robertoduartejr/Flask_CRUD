
from sqlalchemy_utils import ChoiceType, EmailType
from app import db


class Torcedor(db.Model):
    TYPES = [
        ('Vasco', 'Vasco'),
        ('flamengo', 'Flamengo'),
        ('fluminense', 'Fluminense'),
        ('botafogo', 'Botafogo'),
        ('palmeiras', 'Palmeiras'),
        ('sao paulo', 'São Paulo'),
        ('corinthians', 'Corinthians'),
        ('santos', 'Santos'),
        ('cruzeiro', 'Cruzeiro'),
        ('atletico mineiro', 'Atlético Mineiro'),
        ('internacional', 'Internacional'),
        ('gremio', 'Grêmio'),
        ('goias', 'Goiás'),
        ('atlético goianiense', 'Atlético Goianiense'),
        ('outro', 'Outro'),
    ]

    #__tablename__ = 'torcedores'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))
    data_nascimento = db.Column(db.DateTime)
    time = db.Column(ChoiceType(TYPES))
    email = db.Column(EmailType, unique=True)
    cpf = db.Column(db.String(14), unique=True)

    def __init__(self,nome,data_nascimento,time,email,cpf):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.time = time
        self.email = email
        self.cpf = cpf