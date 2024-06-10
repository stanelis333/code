


from Klases.biblioteka import Biblioteka
from Klases.papildomi_def import gauti_skaitmenini_pasirikima
from views import pirmas_meniu, antras_meniu, trecias_meniu, ketvirtas_meniu, penktas_meniu

def main():
    biblioteka = Biblioteka()
    while True:
        print(pirmas_meniu())
        pasirinkimas = gauti_skaitmenini_pasirikima("Pasirinkite: ", [1, 2, 3])
        if pasirinkimas == 1:
            vartotojo_tipas = gauti_skaitmenini_pasirikima("\nPasirinkite vartotojo tipą:\n\n1. Skaitytojas\n2. Bibliotekininkas\n", [1, 2])
            if vartotojo_tipas == 1:
                ID = input("Įveskite savo ID: ")
                skaitytojas = biblioteka.gauti_skaitytoja(ID)
                if skaitytojas:
                    while True:
                        print(antras_meniu())
                        skaitytojo_pasirinkimas = gauti_skaitmenini_pasirikima("Pasirinkite: ", [1, 2, 3, 4, 5, 6])
                        if skaitytojo_pasirinkimas == 1:
                            print(trecias_meniu())
                            pasirinkimas = gauti_skaitmenini_pasirikima("Pasirinkite: ", [1, 2])
                            if pasirinkimas == 1:
                                autorius = input("Įveskite autorių: ")
                                rezultatai = biblioteka.ieskoti_knygu(autorius=autorius)
                                if rezultatai:
                                    for knyga in rezultatai:
                                        print(knyga)
                                else:
                                    print("Atsiprašome, nieko nepavyko rasti.")
                            elif pasirinkimas == 2:
                                pavadinimas = input("Įveskite pavadinimą: ")
                                rezultatai = biblioteka.ieskoti_knygu(pavadinimas=pavadinimas)
                                if rezultatai:
                                    for knyga in rezultatai:
                                        print(knyga)
                                else:
                                    print("Atsiprašome, nieko nepavyko rasti.")
                        elif skaitytojo_pasirinkimas == 2:
                            pavadinimas = input("Įveskite knygos pavadinimą: ")
                            biblioteka.paimti_knyga(ID, pavadinimas)
                        elif skaitytojo_pasirinkimas == 3:
                            pavadinimas = input("Įveskite knygos pavadinimą: ")
                            biblioteka.grazinti_knyga(ID, pavadinimas)
                        elif skaitytojo_pasirinkimas == 4:
                            biblioteka.perziureti_visas_knygas()
                        elif skaitytojo_pasirinkimas == 5:
                            biblioteka.perziureti_veluojancias_knygas()
                        elif skaitytojo_pasirinkimas == 6:
                            break
                else:
                    print("\nToks ID neegzistuoja.")
            elif vartotojo_tipas == 2:
                vardas = input("Įveskite vardą: ")
                slaptazodis = input("Įveskite slaptažodį: ")
                bibliotekininkas = biblioteka.gauti_bibliotekininka(vardas, slaptazodis)
                if bibliotekininkas:
                    while True:
                        print(ketvirtas_meniu())
                        bibliotekininko_pasirinkimas = gauti_skaitmenini_pasirikima("Pasirinkite: ", [1, 2, 3, 4, 5, 6])
                        if bibliotekininko_pasirinkimas == 1:
                            autorius = input("Įveskite autorių: ")
                            pavadinimas = input("Įveskite pavadinimą: ")
                            zanras = input("Įveskite žanrą: ")
                            while True:
                                metai = input("Įveskite metus: ")
                                if metai.isdigit():
                                    break
                                else:
                                    print("Patikslinkite knygos metus, galimi tik skaičiai..")
                            while True:
                                kiekis = input("Įveskite kiekį: ")
                                if kiekis.isdigit():
                                    break
                                else:
                                    print("Patikslinkite kiekį, galimi tik skaičiai..")
                            biblioteka.prideti_knyga(autorius, pavadinimas, zanras, metai, kiekis)
                        elif bibliotekininko_pasirinkimas == 2:
                            while True:
                                metai = input("Įveskite metus, senesnės knygos bus pašalintos: ")
                                if metai.isdigit():
                                    break
                                else:
                                    print("Patikslinkite metus, galimi tik skaičiai..")
                            
                            biblioteka.pasalinti_knygas(metai)
                        elif bibliotekininko_pasirinkimas == 3:
                            print(penktas_meniu())
                            pasirinkimas = gauti_skaitmenini_pasirikima("Pasirinkite: ", [1, 2])
                            if pasirinkimas == 1:
                                autorius = input("Įveskite autorių: ")
                                rezultatai = biblioteka.ieskoti_knygu(autorius=autorius)
                                if rezultatai:
                                    for knyga in rezultatai:
                                        print(knyga)
                                else:
                                    print("Atsiprašome, nieko nepavyko rasti.")
                            elif pasirinkimas == 2:
                                pavadinimas = input("Įveskite pavadinimą: ")
                                rezultatai = biblioteka.ieskoti_knygu(pavadinimas=pavadinimas)
                                if rezultatai:
                                    for knyga in rezultatai:
                                        print(knyga)
                                else:
                                    print("Atsiprašome, nieko nepavyko rasti.")
                        elif bibliotekininko_pasirinkimas == 4:
                            biblioteka.perziureti_visas_knygas()
                        elif bibliotekininko_pasirinkimas == 5:
                            biblioteka.perziureti_veluojancias_knygas()
                        elif bibliotekininko_pasirinkimas == 6:
                            break
                else:
                    print("Neteisingas vardas arba slaptažodis.")
        elif pasirinkimas == 2:
            vartotojo_tipas = gauti_skaitmenini_pasirikima("\nRegistruoti kaip:\n\n1. Skaitytoją\n2. Bibliotekininką\n", [1, 2])
            if vartotojo_tipas == 1:
                ID = input("Įveskite savo ID: ")
                if biblioteka.gauti_skaitytoja(ID):
                    print(f"\nSkaitytojas su ID: ({ID})  jau yra užregistruotas, pabandykite kitą variantą.")
                else:
                    biblioteka.registruoti_skaitytoja(ID)
                    print(f"Skaitytojas su ID: ({ID}) užregistruotas.")
            elif vartotojo_tipas == 2:
                vardas = input("Įveskite vardą: ")
                slaptazodis = input("Įveskite slaptažodį: ")
                if biblioteka.gauti_bibliotekininka(vardas, slaptazodis):
                    print(f"Bibliotekininkas ({vardas}) jau egzistuoja, pabandykite kitą variantą.")
                else:
                    biblioteka.registruoti_bibliotekininka(vardas, slaptazodis)
                    print(f"Bibliotekininkas ({vardas}) užregistruotas.")
        elif pasirinkimas == 3:
            print("\nIšeinama iš programos...")
            break

if __name__ == "__main__":
    main()
    