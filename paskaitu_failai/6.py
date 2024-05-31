# class Transportas:
#     def __init__(self, ratai, metai, greitis = None):
#         self.ratai = ratai
#         self.metai = metai
#         if greitis:
#             self.greitis = greitis

#     def __str__(self):
#         return f"Ratai: {self.ratai}, Greitis: {self.greitis}, Metai: {self.metai}"

#     def vaziuoju(self):
#         print("Wrromm wromm")

# class Motociklas(Transportas):
#     def vaziuoju(self):
#         print("DZIIUMMM")

# class Masina(Transportas):
#     def __init__(self, ratai, metai, spalva):
#         self.spalva = spalva
#         super().__init__(ratai, metai)

#     # def __init__(self, transportas, spalva):
#     #     super().__init__(transportas.ratai, transportas.greitis, transportas.metai)
#     #     self.spalva = spalva

#     def __str__(self):
#         return f"Ratai: {self.ratai}, Metai: {self.metai}, Spalva: {self.spalva}"


# transporto_priemones = []

# transportas = Transportas(4, 1998,120)
# motociklas = Motociklas(2, 2005, 280)
# masina = Masina(4, 2005, "Juoda")
# # masina = Masina(transportas, "Juoda")

# transporto_priemones.append(transportas)
# transporto_priemones.append(motociklas)
# transporto_priemones.append(masina)

# for transporto_priemone_viena in transporto_priemones:
#     print(transporto_priemone_viena)
#     transporto_priemone_viena.vaziuoju()
#     print()

# # transportas.vaziuoju()
# # motociklas.vaziuoju()
# # masina.vaziuoju()
