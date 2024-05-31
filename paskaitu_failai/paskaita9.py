

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
    def __init__(self, vardas):
        self.vardas = vardas
        self.paimtos_knygos = {}

    def __str__(self):
        return f"Vardas: {self.vardas}, Paimtų knygų kiekis: {len(self.paimtos_knygos)}"

class Biblioteka:
    def __init__(self, knygos_failas, skaitytojai_failas):
        self.knygos_failas = knygos_failas
        self.skaitytojai_failas = skaitytojai_failas
        self.knygos = self.uzkrauti_duomenis(knygos_failas)
        self.skaitytojai = self.uzkrauti_duomenis(skaitytojai_failas)

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
        knyga = Knyga(autorius, pavadinimas, zanras, metai, kiekis)
        self.knygos.append(knyga)
        self.issaugoti_duomenis(self.knygos_failas, self.knygos)

    def pasalinti_knygas(self, metai):
        self.knygos = [knyga for knyga in self.knygos if knyga.metai >= metai]
        self.issaugoti_duomenis(self.knygos_failas, self.knygos)

    def ieskoti_knygu(self, autorius=None, pavadinimas=None):
        rezultatai = []
        for knyga in self.knygos:
            if autorius and autorius.lower() in knyga.autorius.lower():
                rezultatai.append(knyga)
            elif pavadinimas and pavadinimas.lower() in knyga.pavadinimas.lower():
                rezultatai.append(knyga)
        return rezultatai

    def paimti_knyga(self, skaitytojo_vardas, pavadinimas):
        skaitytojas = self.gauti_skaitytoja(skaitytojo_vardas)
        if any(datetime.datetime.now() > data for data in skaitytojas.paimtos_knygos.values()):
            print(f"{skaitytojo_vardas} turi vėluojančių knygų!")
            return
        for knyga in self.knygos:
            if knyga.pavadinimas.lower() == pavadinimas.lower() and knyga.paimta < knyga.kiekis:
                knyga.paimta += 1
                gražinimo_data = datetime.datetime.now() + datetime.timedelta(days=14)
                skaitytojas.paimtos_knygos[knyga.pavadinimas] = gražinimo_data
                self.issaugoti_duomenis(self.knygos_failas, self.knygos)
                self.issaugoti_duomenis(self.skaitytojai_failas, self.skaitytojai)
                print(f"Knyga '{knyga.pavadinimas}' paimta iki {gražinimo_data}")
                return
        print(f"Knyga '{pavadinimas}' nerasta arba nėra laisvų kopijų.")

    def grazinti_knyga(self, skaitytojo_vardas, pavadinimas):
        skaitytojas = self.gauti_skaitytoja(skaitytojo_vardas)
        if pavadinimas in skaitytojas.paimtos_knygos:
            del skaitytojas.paimtos_knygos[pavadinimas]
            for knyga in self.knygos:
                if knyga.pavadinimas == pavadinimas:
                    knyga.paimta -= 1
                    self.issaugoti_duomenis(self.knygos_failas, self.knygos)
                    self.issaugoti_duomenis(self.skaitytojai_failas, self.skaitytojai)
                    print(f"Knyga '{pavadinimas}' grąžinta.")
                    return
        print(f"Skaitytojas '{skaitytojo_vardas}' neturi paimtos knygos '{pavadinimas}'.")

    def perziureti_visas_knygas(self):
        for knyga in self.knygos:
            print(knyga)

    def perziureti_veluojancias_knygas(self):
        for skaitytojas in self.skaitytojai:
            for pavadinimas, data in skaitytojas.paimtos_knygos.items():
                if datetime.datetime.now() > data:
                    print(f"{skaitytojas.vardas} vėluoja grąžinti knygą '{pavadinimas}', kuri turėjo būti grąžinta iki {data}.")

    def gauti_skaitytoja(self, vardas):
        for skaitytojas in self.skaitytojai:
            if skaitytojas.vardas == vardas:
                return skaitytojas
        naujas_skaitytojas = Skaitytojas(vardas)
        self.skaitytojai.append(naujas_skaitytojas)
        self.issaugoti_duomenis(self.skaitytojai_failas, self.skaitytojai)
        return naujas_skaitytojas

def main():
    biblioteka = Biblioteka("knygos.pkl", "skaitytojai.pkl")
    while True:
        print("\n1. Pridėti naują knygą")
        print("2. Pašalinti senas knygas")
        print("3. Ieškoti knygų")
        print("4. Pasiimti knygą")
        print("5. Grąžinti knygą")
        print("6. Peržiūrėti visas knygas")
        print("7. Peržiūrėti vėluojančias knygas")
        print("8. Išeiti iš programos")
        pasirinkimas = input("Pasirinkite: ")
        if pasirinkimas == "1":
            autorius = input("Įveskite autorių: ")
            pavadinimas = input("Įveskite pavadinimą: ")
            zanras = input("Įveskite žanrą: ")
            metai = int(input("Įveskite metus: "))
            kiekis = int(input("Įveskite kiekį: "))
            biblioteka.prideti_knyga(autorius, pavadinimas, zanras, metai, kiekis)
        elif pasirinkimas == "2":
            metai = int(input("Pašalinti knygas senesnes nei metai: "))
            biblioteka.pasalinti_knygas(metai)
        elif pasirinkimas == "3":
            print("Ieškoti pagal: ")
            print("1. Autorių")
            print("2. Pavadinimą")
            pasirinkimas_ieskoti = input("Pasirinkite: ")
            if pasirinkimas_ieskoti == "1":
                autorius = input("Įveskite autorių: ")
                rezultatai = biblioteka.ieskoti_knygu(autorius=autorius)
            elif pasirinkimas_ieskoti == "2":
                pavadinimas = input("Įveskite pavadinimą: ")
                rezultatai = biblioteka.ieskoti_knygu(pavadinimas=pavadinimas)
            for knyga in rezultatai:
                print(knyga)
        elif pasirinkimas == "4":
            skaitytojo_vardas = input("Įveskite savo vardą: ")
            pavadinimas = input("Įveskite knygos pavadinimą: ")
            biblioteka.paimti_knyga(skaitytojo_vardas, pavadinimas)
        elif pasirinkimas == "5":
            skaitytojo_vardas = input("Įveskite savo vardą: ")
            pavadinimas = input("Įveskite knygos pavadinimą: ")
            biblioteka.grazinti_knyga(skaitytojo_vardas, pavadinimas)
        elif pasirinkimas == "6":
            biblioteka.perziureti_visas_knygas()
        elif pasirinkimas == "7":
            biblioteka.perziureti_veluojancias_knygas()
        elif pasirinkimas == "8":
            break
        else:
            print("Neteisingas pasirinkimas, bandykite dar kartą.")

if __name__ == "__main__":
    main()
