# Modelo para o banco de dados

from flask_sqlalchemy import SQLAlchemy # Biblioteca que ajuda a gerenciar bancos de dados em Python, permitindo criar e manipular tabelas usando classes e objetos Python

db = SQLAlchemy() # É a instância principal do SQLAlchemy, que será conectada ao aplicativo Flask no arquivo principal (app.py)

class Task(db.Model): # Representa uma tabela chamada Task no banco de dados
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)