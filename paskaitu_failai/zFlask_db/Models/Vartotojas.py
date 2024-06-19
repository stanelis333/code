from database import db
from sqlalchemy.orm import relationship

class Vartotojas(db.Model):
    __tablename__ = "Vartotojai"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    masinos = relationship("Masinos", back_populates="vartotojas")

    def __init__(self, name):
        self.name = name
