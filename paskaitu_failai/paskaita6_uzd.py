########################################################### Uzduotis nr.1

# class Automobilis:
#     def __init__(self, metai, modelis, kuro_tipas):
#         self.metai = metai
#         self.modelis = modelis
#         self.kuro_tipas = kuro_tipas

#     def vaziuoti(self):
#         return("vaziuoja ")
#     def stoveti(self):
#         return("priparkuota ")
#     def pildyti_degalus(self):
#         return("degalai ipilti ")
#     def __str__(self):
#         return f"{self.metai} | {self.modelis} | {self.kuro_tipas}"

# class Elektromobilis(Automobilis):
#     def pildyti_degalus(self):
#         return("baterija ikrauta ")
#     def vaziuoti_autonomiskai(self):
#         return "vaziuoja autonomiskai "


# automobilis = Automobilis(2013, "audi", "benzinas")
# elektromobilis = Elektromobilis(2022, "Tesla", "Elektra")

# # print(automobilis)
# # print(automobilis.vaziuoti())
# # print(automobilis.stoveti())
# # print(automobilis.pildyti_degalus())

# # print(elektromobilis)
# # print(elektromobilis.vaziuoti())
# # print(elektromobilis.stoveti())
# # print(elektromobilis.pildyti_degalus())
# # print(elektromobilis.vaziuoti_autonomiskai())


########################################################### Uzduotis nr.2



# from datetime import datetime
# class Darbuotojas:
#     def __init__(self, vardas, valandos_ikainis, dirba_nuo):
#         self.vardas = vardas
#         self.valandos_ikainis = valandos_ikainis
#         self.dirba_nuo = datetime.strptime(dirba_nuo, '%Y-%m-%d')
#     def _skaiciuoti_dirbtas_dienas(self):
#         dabar = datetime.now()
#         skirtumas = dabar - self.dirba_nuo
#         return skirtumas.days
#     def paskaiciuoti_atlyginima(self):
#         dirbtos_dienos = self._skaiciuoti_dirbtas_dienas()
#         valandos = dirbtos_dienos * 8  
#         atlyginimas = valandos * self.valandos_ikainis
#         return atlyginimas
#     def __str__(self):
#         return(f"Vardas:  {self.vardas} \nValandos ikainis: {self.valandos_ikainis}  \nDirba nuo: {self.dirba_nuo}")
    
   
# class NormalusDarbuotojas(Darbuotojas):
#     def _skaiciuoti_dirbtas_dienas(self):
#         dabar = datetime.now()
#         skirtumas = dabar - self.dirba_nuo
#         savaites = skirtumas.days // 7
#         papildomos_dienos = skirtumas.days % 7
#         dirbtos_dienos = savaites * 5 + min(papildomos_dienos, 5)
#         return dirbtos_dienos
    
   
# darbuotojas = Darbuotojas("Valius", 11, "2024-04-21")    
# normalus_darbuotojas = NormalusDarbuotojas("Sigis", 9, "2024-04-21")  


# # print(darbuotojas)
# print(f"{darbuotojas.vardas} atlyginimas: {darbuotojas.paskaiciuoti_atlyginima()} EUR")

# # print(normalus_darbuotojas)
# print(f"{normalus_darbuotojas.vardas} atlyginimas: {normalus_darbuotojas.paskaiciuoti_atlyginima()} EUR")



########################################################### nr.3



# class Irasas:
#     def __init__(self, suma):
#         self.suma = suma
#     def __str__(self):
#         return f"{self.suma} EUR"
# class Pajamu_irasas(Irasas):
#     def __init__(self, suma, siuntejas, papildoma_informacija):
#         super().__init__(suma)
#         self.siuntejas = siuntejas
#         self.papildoma_informacija = papildoma_informacija
#     def __str__(self):
#        return f"Pajamos: {self.suma} EUR, Siuntėjas: {self.siuntejas}, Informacija: {self.papildoma_informacija}"
# class Islaidu_irasas(Irasas):
#     def __init__(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
#         super().__init__(suma)
#         self.atsiskaitymo_budas = atsiskaitymo_budas
#         self.isigyta_preke_paslauga = isigyta_preke_paslauga
#     def __str__(self):
#         return f"Išlaidos: {self.suma} EUR, Atsiskaitymo būdas: {self.atsiskaitymo_budas}, Prekė/Paslauga: {self.isigyta_preke_paslauga}"
# class Biudzetas:
#     def __init__(self):
#         self.zurnalas = []
#     def prideti_pajamu_irasa(self, suma, siuntejas, papildoma_informacija):
#         pajamos = Pajamu_irasas(suma, siuntejas, papildoma_informacija)
#         self.zurnalas.append(pajamos)
#     def prideti_islaidu_irasa(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
#         islaidos = Islaidu_irasas(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
#         self.zurnalas.append(islaidos)
#     def gauti_balansa(self):
#         pajamos = sum(irasas.suma for irasas in self.zurnalas if isinstance(irasas, Pajamu_irasas))
#         islaidos = sum(irasas.suma for irasas in self.zurnalas if isinstance(irasas, Islaidu_irasas))
#         return pajamos - islaidos
#     def parodyti_ataskaita(self):
#         for irasas in self.zurnalas:
#             print(irasas)
# biudzetas = Biudzetas()
# while True:
#     print("\nPasirinkite veiksmą:")
#     print("1. Įvesti pajamas")
#     print("2. Įvesti išlaidas")
#     print("3. Parodyti balansą")
#     print("4. Parodyti biudžeto ataskaitą")
#     print("5. Išeiti iš programos")
#     pasirinkimas = input("Pasirinkite: ")
#     if pasirinkimas == "1":
#         suma = float(input("Įveskite pajamų sumą: "))
#         siuntejas = input("Įveskite siuntėją: ")
#         papildoma_informacija = input("Įveskite papildomą informaciją: ")
#         biudzetas.prideti_pajamu_irasa(suma, siuntejas, papildoma_informacija)
#     elif pasirinkimas == "2":
#         suma = float(input("Įveskite išlaidų sumą: "))
#         atsiskaitymo_budas = input("Įveskite atsiskaitymo būdą: ")
#         isigyta_preke_paslauga = input("Įveskite įsigytą prekę ar paslaugą: ")
#         biudzetas.prideti_islaidu_irasa(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
#     elif pasirinkimas == "3":
#         balansas = biudzetas.gauti_balansa()
#         print(f"Balansas: {balansas} EUR")
#     elif pasirinkimas == "4":
#         print("Biudžeto ataskaita:")
#         biudzetas.parodyti_ataskaita()
#     elif pasirinkimas == "5":
#         print("Išeinama iš programos.")
#         break
#     else:
#         print("Neteisingas pasirinkimas, bandykite dar kartą.")
##############################



# class Irasas:
#     def __init__(self, tipas, suma):
#         self.tipas = tipas
#         self.suma = suma
#     def __str__(self):
#         return f"{self.tipas}: {self.suma} EUR"

# class Biudzetas:
#     def __init__(self):
#         self.zurnalas = []

#     def prideti_pajamu_irasa(self, suma):
#         pajamos = Irasas("Pajamos", suma)
#         self.zurnalas.append(pajamos)
#     def prideti_islaidu_irasa(self, suma):
#         islaidos = Irasas("Išlaidos", suma)
#         self.zurnalas.append(islaidos)
#     def gauti_balansa(self):
#         pajamos = sum(irasas.suma for irasas in self.zurnalas if irasas.tipas == "Pajamos")
#         islaidos = sum(irasas.suma for irasas in self.zurnalas if irasas.tipas == "Išlaidos")
#         return pajamos - islaidos
#     def parodyti_ataskaita(self):
#         for irasas in self.zurnalas:
#             print(irasas)

# biudzetas = Biudzetas()
# while True:
#         print("\nPasirinkite veiksmą:")
#         print("1. Įvesti pajamas")
#         print("2. Įvesti išlaidas")
#         print("3. Parodyti balansą")
#         print("4. Parodyti biudžeto ataskaitą")
#         print("5. Išeiti iš programos")
#         pasirinkimas = input("Pasirinkite: ")
#         if pasirinkimas == "1":
#            suma = float(input("Įveskite pajamų sumą: "))
#            biudzetas.prideti_pajamu_irasa(suma)
#         elif pasirinkimas == "2":
#             suma = float(input("Įveskite išlaidų sumą: "))
#             biudzetas.prideti_islaidu_irasa(suma)
#         elif pasirinkimas == "3":
#             balansas = biudzetas.gauti_balansa()
#             print(f"Balansas: {balansas} EUR")
#         elif pasirinkimas == "4":
#             print("Biudžeto ataskaita:")
#             biudzetas.parodyti_ataskaita()
#         elif pasirinkimas == "5":
#             print("Išeinama iš programos.")
#             break
#         else:
#            print("Neteisingas pasirinkimas, bandykite dar kartą.")
