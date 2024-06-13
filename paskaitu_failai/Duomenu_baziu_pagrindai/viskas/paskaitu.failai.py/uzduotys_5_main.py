from uzduotys_5 import Employees
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///paskaitu_failai/Duomenu_baziu_pagrindai/db.failai/Darbuotojai_Database.db')
SessionMaker = sessionmaker(bind= engine)
session = SessionMaker()


while True:

    pasirinkimas = input(
    '''
    1. Parodyti visus darbuotojus
    2. Pridėti naują darbuotoja
    3. Surasti darbuotoja pagal id
    4. Pakeisti darbuotojo duomenis
    5. Pašalinti darbuotoja
    6. Uždaryti programą

    Įveskite: '''
    )

    if pasirinkimas == "1":
        employees = session.query(Employees).all()
        for employee in employees:
            print(employee)
    if pasirinkimas == "2":
        name = input("Įveskite darbuotojo vardą: ")
        last_name = input("Įveskite darbuotojo pavarde: ")
        birt_date = input("Įveskite darbuotojo gimimo metus: ")
        position = input("Įveskite darbuotojo pareigas: ")
        salary = input("Įveskite darbuotojo atlyginima: ")
        employee = Employees(name, last_name, birt_date, position, salary)
        session.add(employee)
        session. commit ()

    if pasirinkimas == "3":
        id = int(input("Įveskite darbuotojo id: "))
        employee = session.get(Employees, id)
        print (employee)

    if pasirinkimas == "4":
        id = int(input("Įveskite vartotojo id: "))
        pasirinkimas_keisti = input('\nKą norėtumėte keisti?\n1. Vardą\n2. Pavardę\n3. Gimimo metus\n4. Pareigas\n5. Atlyginimą \n\nĮveskite:')        
        employee = session.get(Employees, id)

        if pasirinkimas_keisti == "1":
            new_name = input("Įveskite naują darbuotojo vardą: ")           
            employee.name = new_name

        if pasirinkimas_keisti == "2":
            new_last_name = input("Įveskite naują vartotojo Pavardę: ")
            employee.last_name = new_last_name

        if pasirinkimas_keisti == "3":
            new_bday = input("Įveskite naują darbuotojo gimimo data: ")
            employee.birth_date = new_bday

        if pasirinkimas_keisti == "4":
            new_position = input("Įveskite naujas dabuotojo pareigas: ")
            employee.position = new_position

        if pasirinkimas_keisti == "5":
            new_salary = input("Įveskite naują darbuotojo atlyginima: ")
            employee.salary = new_salary

        session.commit ()

    if pasirinkimas == "5":
        id = int(input("Įveskite šalinamo darbuotojo id: "))

        employee = session.get(Employees, id)
        session.delete(employee)
        session.commit ()

    if pasirinkimas == "6":
        print("Išeinama iš programos.. ")
        break