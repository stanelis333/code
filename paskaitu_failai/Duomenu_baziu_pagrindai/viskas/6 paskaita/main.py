from crud import *



while True:
    pasirinkimas = input(
        '''
    1. Atspausdink visus vartotojus
    2. Sukurk naują vartotoją
    3. Atspausdink visus roles
    4. Sukurk naują role
    5. Priskirti vartotojui role
    6. Atspausdink vartotojo roles
    7. Išrašyti sąskaitą
    8. Atspausdinti vartotojo sąskaitas

    Įveskite: '''
    )

    if pasirinkimas == "1":
        users = get_all_users()
        for user in users:
            print(user.name)

    if pasirinkimas == "2":
        vardas = input("Įveskite vartotojo vardą: ")
        amzius = int(input("Įveskite vartotojo amžių: "))

        create_user(vardas, amzius)

    if pasirinkimas == "3":
        roles = get_all_roles()
        for role in roles:
            print(role)

    

    if pasirinkimas == "5":
        user_id = input("Įveskite vartotojo id: ")
        role_id = input("Įveskite roles id: ")

        add_role_to_user(user_id, role_id)

    if pasirinkimas == "6":
        user_id = input("Įveskite vartotojo id: ")

        roles = get_user_roles(user_id)
        print(f"Vartotojas {user_id} turi roles:")
        for role in roles:
            print(role)

    if pasirinkimas == "7":
        user_id = input("Įveskite vartotojo id: ")
        pavadinimas = input("Įveskite sąskaitos pavadinima: ")

        create_invoice(pavadinimas, user_id)

    if pasirinkimas == "8":
        user_id = input("Įveskite vartotojo id: ")

        invoices = get_all_invoices_by_user_id(user_id)
        print(f"Vartotojas {user_id} turi sąskaitas:")
        for invoice in invoices:
            print(invoice)

        