from database import db, app
from Models.Vartotojas import Vartotojas
from Models.Masinos import Masinos

with app.app_context():
    db.create_all()

    rokas = Vartotojas("Rokas")
    jonas = Vartotojas("Jonas")
    diana = Vartotojas("Diana")
    masina1 = Masinos("Audi")
    masina2 = Masinos("Bmw")
    masina3 = Masinos("Opel")

    db.session.add_all([rokas, jonas, diana, masina1, masina2, masina3])
    db.session.commit()

