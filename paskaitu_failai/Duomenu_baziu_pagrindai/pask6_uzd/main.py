
from crud import *

while True:

    pasirinkimas = input(
    '''
    1. Parodyti visus darbuotojus
    2. Pridėti naują darbuotoja
    3. Surasti darbuotoja pagal id
    4. Pakeisti darbuotojo duomenis
    5. Pašalinti darbuotoja
    6. Sukurti nauja projekta
    7. Parodyti visus projektus
    8. Priskirti darbuotoja prie projekto
    9. Parodyti priskirtus darbuotojus prie projektu
    10. Sukurti nauja departamenta
    11. Priskirti darbuotoja prie departamento
    0. Uždaryti programą

    Įveskite: '''
    )

    if pasirinkimas == "11":
        empl_id = input("Įveskite darbuotojo id: ")
        dep_id = input("Įveskite departamento id: ")
        add_empl_to_dep(empl_id, dep_id)

    if pasirinkimas == "10":
        dep = input("Įveskite nauja departamenta: ")
        create_dep(dep)

    if pasirinkimas == "9":
        emp = input("Įveskite darbuotojo id: ")
        employs = get_empl_proj(emp)
        for employ in employs:
            print(employ)

    if pasirinkimas == "6":
        proj = input("Įveskite nauja projekta: ")
        create_proj(proj)

    if pasirinkimas == "7":
        projects = get_all_proj()
        for project in projects:
            print(project)

    if pasirinkimas == "8":
        empl_id = input("Įveskite darbuotojo id: ")
        proj_id = input("Įveskite projekto id: ")
        add_empl_to_proj(empl_id, proj_id)


    if pasirinkimas == "1":
        employs = get_all_employ()
        for employ in employs:
            print(employ)
    if pasirinkimas == "2":
        name = input("Įveskite darbuotojo vardą: ")
        last_name = input("Įveskite darbuotojo pavarde: ")
        birt_date = input("Įveskite darbuotojo gimimo metus: ")
        position = input("Įveskite darbuotojo pareigas: ")
        salary = input("Įveskite darbuotojo atlyginima: ")
        create_employ(name,last_name,birt_date,position,salary)

    if pasirinkimas == "3":
        id = int(input("Įveskite darbuotojo id: "))
        employee = session.get(Employee, id)
        print (employee)

    if pasirinkimas == "4":
        id = int(input("Įveskite vartotojo id: "))
        pasirinkimas_keisti = input('\nKą norėtumėte keisti?\n1. Vardą\n2. Pavardę\n3. Gimimo metus\n4. Pareigas\n5. Atlyginimą \n\nĮveskite:')        
        employee = session.get(Employee, id)

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

        employee = session.get(Employee, id)
        session.delete(employee)
        session.commit ()

    if pasirinkimas == "0":
        print("Išeinama iš programos.. ")
        break