
from database import db


class Vartotojas(db.Model):
    __tablename__ = 'Vartotojai'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age