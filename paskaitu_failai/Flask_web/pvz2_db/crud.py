from database import db
from Models.vartotojas import Vartotojas

def sukurti_vartotoja(name, age):
    vartotojas = Vartotojas(name, age)

    db.session.add(vartotojas)
    db.session.commit()

def gauti_visus_vartotojus():
    vartotojai = db.session.query(Vartotojas).all()
    return vartotojai
