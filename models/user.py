
from Database import db
from flask_login import UserMixin

class User(db.Model,UserMixin):
    #mapeamento de informações
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80),nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)