

from Biudzetas import biudzetas

biudzetas1 = biudzetas()
while True:
    print("\nPasirinkite veiksmą:")
    print("1. Įvesti pajamas")
    print("2. Įvesti išlaidas")
    print("3. Parodyti balansą")
    print("4. Parodyti biudžeto ataskaitą")
    print("5. Išeiti iš programos")
    pasirinkimas = input("Pasirinkite: ")
    if pasirinkimas == "1":
        suma = float(input("Įveskite pajamų sumą: "))
        siuntejas = input("Įveskite siuntėją: ")
        papildoma_informacija = input("Įveskite papildomą informaciją: ")
        biudzetas1.prideti_pajamu_irasa(suma, siuntejas, papildoma_informacija)
    elif pasirinkimas == "2":
        suma = float(input("Įveskite išlaidų sumą: "))
        atsiskaitymo_budas = input("Įveskite atsiskaitymo būdą: ")
        isigyta_preke_paslauga = input("Įveskite įsigytą prekę ar paslaugą: ")
        biudzetas1.prideti_islaidu_irasa(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
    elif pasirinkimas == "3":
        balansas = biudzetas1.gauti_balansa()
        print(f"Balansas: {balansas} EUR")
    elif pasirinkimas == "4":
        print("Biudžeto ataskaita:")
        biudzetas1.parodyti_ataskaita()
    elif pasirinkimas == "5":
        print("Išeinama iš programos.")
        break
    else:
        print("Neteisingas pasirinkimas, bandykite dar kartą.")