from paskaita5 import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///paskaitu_failai/Duomenu_baziu_pagrindai/db.failai/Vartotojai_Database.db')
SessionMaker = sessionmaker(bind= engine)
session = SessionMaker()


while True:

    pasirinkimas = input(
    '''
    1. Atspausdink visus vartotojus
    2. Sukurk naują vartotoją
    3. Surask pagal id
    4. Pakeisti vartotoją
    5. Pašalinti vartotoją

    Įveskite: '''
    )

    if pasirinkimas == "1":
        users = session.query(User).all()
        for user in users:
            print(user)

    if pasirinkimas == "2":
        vardas = input("Įveskite vartotojo vardą: ")
        amzius = int(input("Įveskite vartotojo amžių: "))
        user = User(vardas, amzius)
        session.add(user)
        session. commit ()

    if pasirinkimas == "3":
        id = int(input("Įveskite vartotojo id: "))
        user = session.get(User, id)
        print (user)

    if pasirinkimas == "4":
        id = int(input("Įveskite vartotojo id: "))

        pasirinkimas_keisti = input('''
Ką norėtumėte keisti?

1. Vardą
2. Amžių

Įveskite:
''')

        
        user = session.get(User, id)

        if pasirinkimas_keisti == "1":
            naujas_vardas = input("Įveskite naują vartotojo vardą: ")
            
            user.name = naujas_vardas
        if pasirinkimas_keisti == "2":
            naujas_amzius = int(input("Įveskite naują vartotojo amžių: "))
            user.age = naujas_amzius

        session.commit ()

    if pasirinkimas == "5":
        id = int(input("Įveskite šalinamo vartotojo id: "))

        user = session.get(User, id)
        session.delete(user)
        session.commit ()