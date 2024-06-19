from database import db
from sqlalchemy.orm import relationship

class Masinos(db.Model):
    __tablename__ = "Masinos"
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String)
    model = db.Column(db.String)
    year = db.Column(db.Integer)
    vartotojas_id = db.Column(db.Integer, db.ForeignKey('Vartotojai.id'))
    vartotojas = relationship("Vartotojas", back_populates="masinos")

    def __init__(self, brand, model = None, year= None):
        self.brand = brand
        self.model = model
        self.year = year
