from database import db
from Models.Vartotojas import Vartotojas
from Models.Masinos import Masinos

# ----------------------------------------Vartotojas CRUD
def sukurti_vartotoja(name):
    vartotojas = Vartotojas(name)
    db.session.add(vartotojas)
    db.session.commit()

def gauti_visus_vartotojus():
    return db.session.query(Vartotojas).all()

def gauti_vartotoja(id):
    return db.session.get(Vartotojas, id)

def istrinti_vartotoja(id):
    vartotojas = gauti_vartotoja(id)
    db.session.delete(vartotojas)
    db.session.commit()

def atnaujinti_vartotoja(id, name):
    vartotojas = gauti_vartotoja(id)
    vartotojas.name = name
    db.session.commit()

#-------------------------------------------- Masinos CRUD
def gauti_masina(id):
    return db.session.get(Masinos, id)

def gauti_visas_masinas():
    return db.session.query(Masinos).all()

def sukurti_masina(brand, model, year):
    masina = Masinos(brand, model, year)
    db.session.add(masina)
    db.session.commit()


def priskirti_masina_vartotojui(car_id, vartotojo_id):
    masina = gauti_masina(car_id)
    vartotojas = gauti_vartotoja(vartotojo_id)
    if masina and vartotojas:
        masina.vartotojas_id = vartotojo_id
        db.session.commit()
        return True
    return False

def istrinti_masina(id):
    masina = gauti_masina(id)
    if masina:
        db.session.delete(masina)
        db.session.commit()
        return True
    return False
