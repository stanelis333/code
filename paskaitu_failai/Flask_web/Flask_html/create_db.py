from database import db, app
from Models.Vartotojas import Vartotojas

with app.app_context():
    db.create_all()

    rokas = Vartotojas("Rokas", 99)
    jonas = Vartotojas("Jonas", 55)
    diana = Vartotojas("Diana", 44)

    db.session.add_all([rokas, jonas, diana])
    db.session.commit()


