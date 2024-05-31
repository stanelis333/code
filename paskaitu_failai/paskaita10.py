

import pickle
import os
import datetime

class Knyga:
    def __init__(self, autorius, pavadinimas, zanras, metai, kiekis):
        self.autorius = autorius
        self.pavadinimas = pavadinimas
        self.zanras = zanras
        self.metai = metai
        self.kiekis = kiekis
        self.paimta = 0

    def __str__(self):
        return f"Autorius: {self.autorius}, Pavadinimas: {self.pavadinimas}, Žanras: {self.zanras}, Metai: {self.metai}, Kiekis: {self.kiekis}, Paimta: {self.paimta}"

class Skaitytojas:
    def __init__(self, ID):
        self.ID = ID
        self.paimtos_knygos = {}

    def __str__(self):
        return f"ID: {self.ID}, Paimtų knygų kiekis: {len(self.paimtos_knygos)}"

class Bibliotekininkas:
    def __init__(self, vardas, slaptazodis):
        self.vardas = vardas
        self.slaptazodis = slaptazodis

    def __str__(self):
        return f"Bibliotekininkas: {self.vardas}"

class Biblioteka:
    def __init__(self, knygos_failas, skaitytojo_failas, bibliotekininko_failas):
        self.knygos_failas = knygos_failas
        self.skaitytojo_failas = skaitytojo_failas
        self.bibliotekininko_failas = bibliotekininko_failas
        self.knygos = self.uzkrauti_duomenis(knygos_failas)
        self.skaitytojai = self.uzkrauti_duomenis(skaitytojo_failas)
        self.bibliotekininkai = self.uzkrauti_duomenis(bibliotekininko_failas)

    def uzkrauti_duomenis(self, failas):
        if os.path.exists(failas):
            with open(failas, 'rb') as f:
                return pickle.load(f)
        else:
            return []

    def issaugoti_duomenis(self, failas, duomenys):
        with open(failas, 'wb') as f:
            pickle.dump(duomenys, f)

    def prideti_knyga(self, autorius, pavadinimas, zanras, metai, kiekis):
        knyga = Knyga(autorius, pavadinimas, zanras, int(metai), kiekis)
        self.knygos.append(knyga)
        self.issaugoti_duomenis(self.knygos_failas, self.knygos)
        print(f"Knyga:  '{pavadinimas}' pridėta sėkmingai!")

    def pasalinti_knygas(self, metai):
        self.knygos = [knyga for knyga in self.knygos if knyga.metai >= int(metai)]
        self.issaugoti_duomenis(self.knygos_failas, self.knygos)

    def ieskoti_knygu(self, autorius=None, pavadinimas=None):
        rezultatai = []
        for knyga in self.knygos:
            if autorius and autorius.lower() in knyga.autorius.lower():
                rezultatai.append(knyga)
            if pavadinimas and pavadinimas.lower() in knyga.pavadinimas.lower():
                rezultatai.append(knyga)
        return rezultatai

    def paimti_knyga(self, skaitytojo_id, pavadinimas):
        skaitytojas = self.gauti_skaitytoja(skaitytojo_id)
        if any(datetime.datetime.now() > data for data in skaitytojas.paimtos_knygos.values()):
            print(f"Skaitytojas {skaitytojo_id} turi vėluojančių knygų!")
            return
        for knyga in self.knygos:
            if knyga.pavadinimas.lower() == pavadinimas.lower() and knyga.paimta < knyga.kiekis:
                knyga.paimta += 1
                grazinimo_data = datetime.datetime.now() + datetime.timedelta(days=14)
                skaitytojas.paimtos_knygos[knyga.pavadinimas] = grazinimo_data
                self.issaugoti_duomenis(self.knygos_failas, self.knygos)
                self.issaugoti_duomenis(self.skaitytojo_failas, self.skaitytojai)
                print(f"Knyga '{knyga.pavadinimas}' paimta iki {grazinimo_data}")
                return
        print(f"Knyga '{pavadinimas}' nerasta arba nėra laisvų kopijų.")

    def grazinti_knyga(self, skaitytojo_id, pavadinimas):
        skaitytojas = self.gauti_skaitytoja(skaitytojo_id)
        if pavadinimas in skaitytojas.paimtos_knygos:
            del skaitytojas.paimtos_knygos[pavadinimas]
            for knyga in self.knygos:
                if knyga.pavadinimas == pavadinimas:
                    knyga.paimta -= 1
                    self.issaugoti_duomenis(self.knygos_failas, self.knygos)
                    self.issaugoti_duomenis(self.skaitytojo_failas, self.skaitytojai)
                    print(f"Knyga '{pavadinimas}' grąžinta.")
                    return
        print(f"Skaitytojas '{skaitytojo_id}' neturi paimtos knygos '{pavadinimas}'.")

    def perziureti_visas_knygas(self):
        for knyga in self.knygos:
            print(knyga)

    def perziureti_veluojancias_knygas(self):
        for skaitytojas in self.skaitytojai:
            for pavadinimas, data in skaitytojas.paimtos_knygos.items():
                if datetime.datetime.now() > data:
                    print(f"Skaitytojas {skaitytojas.ID} vėluoja grąžinti knygą '{pavadinimas}', kuri turėjo būti grąžinta iki {data}.")

    def gauti_skaitytoja(self, ID):
        for skaitytojas in self.skaitytojai:
            if skaitytojas.ID == ID:
                return skaitytojas
        return None

    def registruoti_skaitytoja(self, ID):
        naujas_skaitytojas = Skaitytojas(ID)
        self.skaitytojai.append(naujas_skaitytojas)
        self.issaugoti_duomenis(self.skaitytojo_failas, self.skaitytojai)
        return naujas_skaitytojas

    def gauti_bibliotekininka(self, vardas, slaptazodis):
        for bibliotekininkas in self.bibliotekininkai:
            if bibliotekininkas.vardas == vardas and bibliotekininkas.slaptazodis == slaptazodis:
                return bibliotekininkas
        return None

    def registruoti_bibliotekininka(self, vardas, slaptazodis):
        naujas_bibliotekininkas = Bibliotekininkas(vardas, slaptazodis)
        self.bibliotekininkai.append(naujas_bibliotekininkas)
        self.issaugoti_duomenis(self.bibliotekininko_failas, self.bibliotekininkai)


def gauti_skaitmenini_pasirikima(pranesimas, galimos_reiksmes):
    while True:
        pasirinkimas = input(pranesimas)
        if pasirinkimas.isdigit() and int(pasirinkimas) in galimos_reiksmes:
            return int(pasirinkimas)
        else:
            print("Galimi tik skaičiai, bandykite dar kartą.")

def main():
    biblioteka = Biblioteka("knygos.pkl", "skaitytojai.pkl", "bibliotekininkai.pkl")
    while True:
        print("\n1. Prisijungti")
        print("2. Registruotis")
        print("3. Išeiti iš programos")
        pasirinkimas = gauti_skaitmenini_pasirikima("Pasirinkite: ", [1, 2, 3])
        if pasirinkimas == 1:
            vartotojo_tipas = gauti_skaitmenini_pasirikima("\nPasirinkite vartotojo tipą:\n\n1. Skaitytojas\n2. Bibliotekininkas\n", [1, 2])
            if vartotojo_tipas == 1:
                ID = input("Įveskite savo ID: ")
                skaitytojas = biblioteka.gauti_skaitytoja(ID)
                if skaitytojas:
                    while True:
                        print("\n1. Ieškoti knygos")
                        print("2. Paimti knygą")
                        print("3. Grąžinti knygą")
                        print("4. Peržiūrėti visas knygas")
                        print("5. Peržiūrėti vėluojančias knygas")
                        print("6. Atsijungti")
                        skaitytojo_pasirinkimas = gauti_skaitmenini_pasirikima("Pasirinkite: ", [1, 2, 3, 4, 5, 6])
                        if skaitytojo_pasirinkimas == 1:
                            print("\nIeškoti pagal: ")
                            print("1. Autorius")
                            print("2. Pavadinimas")
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
                        print("\n1. Pridėti knygą")
                        print("2. Pašalinti knygas")
                        print("3. Ieškoti knygų")
                        print("4. Peržiūrėti visas knygas")
                        print("5. Peržiūrėti vėluojančias knygas")
                        print("6. Atsijungti")
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
                                kiekis = (input("Įveskite kiekį: "))
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
                            print("\nIeškoti pagal: ")
                            print("1. Autorius")
                            print("2. Pavadinimas")
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

