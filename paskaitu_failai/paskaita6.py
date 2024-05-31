


# class Tevas:
#     def __init__(self, vardas, pavarde):
#         self.vardas = vardas
#         self.pavarde = pavarde
#     def __str__(self):
#         return f"{self.vardas} {self.pavarde}"
# class Vaikas(Tevas):
#     def __init__(self, vardas, pavarde, mokymosi_istaiga):
#         super().__init__(vardas, pavarde)
#         self.mokymosi_istaiga = mokymosi_istaiga

# tevas = Tevas("Rokas", "Budreika")
# vaikas = Vaikas("Urtė", "Budreikaitė", "Čiurlionio menų gimnazija")

# # print(tevas)
# # AttributeError: 'Tevas' object has no attribute 'mokymosi_istaiga'

# print(vaikas)
# print(vaikas.mokymosi_istaiga)
# # Čiurlionio menų gimnazija




###############################################################################


# class Irasas:
#     def init_(self, suma):
#         self.suma = suma

# class PajamuIrasas(Irasas):
    

# class IslaiduIrasas(Irasas):
#     pass

# biudzetas = []

# irasas1 = PajamuIrasas(2000)
# irasas2 = IslaiduIrasas(20)
# biudzetas.append(irasas1)
# biudzetas.append(irasas2)

# for x in biudzetas:
#     if isinstance(x, PajamuIrasas):
#         print(x.suma)
#         print("Čia pajamos")
#     elif isinstance(x, IslaiduIrasas):
#         print(x.suma)
#         print("Čia Išlaidos")


###############################################################################

# class transportas:
#     def __init__(self, ratai, greitis, metai):
#         self.ratai = ratai
#         self.greitis = greitis
#         self.metai = metai

#     def vaziuoju(self):
#         print("wroom wroom")

# class motociklas(transportas):
#     def vaziuoju(self):
#         print("dziuumm dzium")

# transportas1 = transportas(4,120,1998)       
# motociklas1 = motociklas(2,280,2005)

# transportas.vaziuoju()
# motociklas.vaziuoju()

#########

# class Transportas:
#     def __init__(self, ratai, greitis, metai):
#         self.ratai = ratai
#         self.greitis = greitis
#         self.metai = metai

#     def vaziuoju(self):
#         print("Wrromm wromm")

# class Motociklas(Transportas):
#     def vaziuoju(self):
#         print("DZIIUMMM")

# class Masina(Transportas):
#     pass


# transportas = Transportas(4, 120, 1998)
# motociklas = Motociklas(2, 280, 2005)
# masina = Masina(2, 280, 2005)

# transportas. vaziuoju()
# motociklas.vaziuoju()
# masina.vaziuoju()















###############################################################################



















###############################################################################