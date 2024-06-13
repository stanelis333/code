



import pickle,os,datetime
from .knyga import Knyga
from .skaitytojas import Skaitytojas
from .bibliotekininkas import Bibliotekininkas

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

    def prideti_knyga(self, autorius, pavadinimas, zanras, metai, kiekis: int):
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
            if knyga.pavadinimas.lower() == pavadinimas.lower() and knyga.paimta < int(knyga.kiekis):
                knyga.paimta += 1
                grazinimo_data = datetime.datetime.now() + datetime.timedelta(minutes=3)
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

    