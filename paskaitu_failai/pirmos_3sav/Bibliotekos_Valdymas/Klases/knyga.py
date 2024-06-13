



class Knyga:
    def __init__(self, autorius, pavadinimas, zanras, metai, kiekis):
        self.autorius = autorius
        self.pavadinimas = pavadinimas
        self.zanras = zanras
        self.metai = metai
        self.kiekis = kiekis
        self.paimta = 0

    def __str__(self):
        return (f"Autorius: {self.autorius}, Pavadinimas: {self.pavadinimas}, Žanras: {self.zanras}, Metai: {self.metai}, Kiekis: {self.kiekis}, Paimta: {self.paimta}")
