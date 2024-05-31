


class Irasas:
    def __init__(self, suma):
        self.suma = suma
    def __str__(self):
        return f"{self.suma} EUR"
class Pajamu_irasas(Irasas):
    def __init__(self, suma, siuntejas, papildoma_informacija):
        super().__init__(suma)
        self.siuntejas = siuntejas
        self.papildoma_informacija = papildoma_informacija
    def __str__(self):
        return f"Pajamos: {self.suma} EUR, Siuntėjas: {self.siuntejas}, Informacija: {self.papildoma_informacija}"
class Islaidu_irasas(Irasas):
    def __init__(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        super().__init__(suma)
        self.atsiskaitymo_budas = atsiskaitymo_budas
        self.isigyta_preke_paslauga = isigyta_preke_paslauga
    def __str__(self):
        return f"Išlaidos: {self.suma} EUR, Atsiskaitymo būdas: {self.atsiskaitymo_budas}, Prekė/Paslauga: {self.isigyta_preke_paslauga}"