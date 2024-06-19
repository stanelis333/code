from database import db, app
from Models.vartotojas import Vartotojas

with app.app_context(): 
    db.create_all()

    Jonas = Vartotojas("Jonas", 77)
    Mantas = Vartotojas("Mantas", 66)
    Nerius = Vartotojas("Nerius", 55)

    db.session.add_all([Jonas, Mantas, Nerius])
    db.session.commit()