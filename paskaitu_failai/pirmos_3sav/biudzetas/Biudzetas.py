from Bendri_irasai import Pajamu_irasas,Islaidu_irasas


class biudzetas:
    def __init__(self):
        self.zurnalas = []
    def prideti_pajamu_irasa(self, suma, siuntejas, papildoma_informacija):
        pajamos = Pajamu_irasas(suma, siuntejas, papildoma_informacija)
        self.zurnalas.append(pajamos)
    def prideti_islaidu_irasa(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        islaidos = Islaidu_irasas(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
        self.zurnalas.append(islaidos)
    def gauti_balansa(self):
        pajamos = sum(irasas.suma for irasas in self.zurnalas if isinstance(irasas, Pajamu_irasas))
        islaidos = sum(irasas.suma for irasas in self.zurnalas if isinstance(irasas, Islaidu_irasas))
        return pajamos - islaidos
    def parodyti_ataskaita(self):
        for irasas in self.zurnalas:
            print(irasas)


