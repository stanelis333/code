from database import db
from Models.Vartotojas import Vartotojas


#------User CRUD-------------------------------------

def sukurti_vartotoja(name, age):
    vartotojas = Vartotojas(name, age)

    db.session.add(vartotojas)
    db.session.commit()

def gauti_visus_vartotojus():
    vartotojai = db.session.query(Vartotojas).all()
    return vartotojai

def gauti_vartotoja(id):
    vartotojas = db.session.get(Vartotojas, id)
    return vartotojas

def istrinti_vartotoja(id):
    vartotojas = db.session.get(Vartotojas, id)
    db.session.delete(vartotojas)
    db.session.commit()

def atnaujinti_vartotoja(id, name, age):
    vartotojas = db.session.get(Vartotojas, id)
    vartotojas.name = name
    vartotojas.age = age
    db.session.commit()