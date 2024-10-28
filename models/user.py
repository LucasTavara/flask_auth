from enum import unique

from app import db

class User(db.Model):
    #mapeamento de informações
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80),nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)