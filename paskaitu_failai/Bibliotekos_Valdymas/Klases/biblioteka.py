



import datetime
from .knyga import Knyga
from .skaitytojas import Skaitytojas
from .bibliotekininkas import Bibliotekininkas
import sqlite3

conn = sqlite3.connect("C:\code\paskaitu_failai\Bibliotekos_Valdymas\Duomenys\Bendri.db")
c = conn.cursor()

class Biblioteka:
    def __init__(self, conn):
        self.conn = conn
        self.knygos = self.uzkrauti_knygos_duomenis(conn)
        self.skaitytojai = self.uzkrauti_skaitytojo_duomenis(conn)
        self.bibliotekininkai = self.uzkrauti_bibliotekininko_duomenis(conn)

    def uzkrauti_knygos_duomenis(self):
        with conn:
            knygos = c.execute("SELECT * FROM Knygos").fetchall()  
            return knygos
    def uzkrauti_skaitytojo_duomenis(self):
        with conn:
            skaitytojai = c.execute("SELECT * FROM Skaitytojai").fetchall() 
            return skaitytojai
    def uzkrauti_bibliotekininko_duomenis(self):
        with conn:
            bibliotekininkai = c.execute("SELECT * FROM Bibliotekininkai").fetchall() 
            return bibliotekininkai
    def issaugoti_knygos_duomenis(knygos):
        with conn:
            c.execute("INSERT INTO Knygos (autorius, pavadinimas, zanras, metai, kiekis) VALUES (?,?,?,?,?)", (knygos.autorius, knygos.pavadinimas, knygos.zanras, knygos.metai, knygos.kiekis))
            
    def issaugoti_skaitytojo_duomenis():
         with conn:
            c.execute("INSERT INTO Skaitytojai (skaitytojo_id, paimtos_knygos) VALUES (?,?)", (conn.ID, conn.paimtos_knygos))
            
    def issaugoti_bibliotekininko_duomenis():
         with conn:
            c.execute("INSERT INTO Bibliotekininkai (vardas, slaptazodis) VALUES (?,?)", (conn.vardas, conn.slaptazodis))
            
    def prideti_knyga(self, autorius, pavadinimas, zanras, metai, kiekis: int):
        knyga = Knyga(autorius, pavadinimas, zanras, int(metai), kiekis)
        self.knygos.append(knyga)
        self.issaugoti_knygos_duomenis(self.knygos)
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

    