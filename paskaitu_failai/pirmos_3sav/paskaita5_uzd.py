# Užduotis nr. 1

# Parašyti klasę Sakinys, kuri turi savybę tekstas ir metodus, kurie:
# · Gražina tekstą atbulai
# · Gražina tekstą mažosiomis raidėmis
# · Gražina tekstą didžiosiomis raidėmis
# · Gražina žodį pagal nurodytą eilės numerį
# · Gražina, kiek tekste yra nurodytų simbolių arba žodžių
# · Gražina tekstą su pakeistu nurodytu žodžiu arba simboliu
# · Atspausdina, kiek sakinyje yra žodžių, skaičių, didžiųjų ir mažųjų raidžių
# Susikurti kelis klasės objektus ir išbandyti visus metodus


                                  ###########   UZDUOTIS NR.1


# class sakinys:
#     def __init__(self, tekstas):
#         self.tekstas = tekstas            
        

#     def atbulai(self):
#         return f"{self.tekstas[::-1]}"
#     def tekstas_mazosiomis(self):
#         return f"{self.tekstas.casefold()}"
#     def tesktas_didziosiomis(self):
#         return f"{self.tekstas.upper()}"
#     def eiles_nr(self, pagal_numeri):
#         pagal_numeri1 = (self.tekstas.split())
#         return pagal_numeri1[pagal_numeri]   
            
#     def paieska(self, surasti):
#         surasti = self.tekstas.count(surasti)
#         return surasti
#     def pakeistas(self, pakeisti1, pakeisti2):
#         return self.tekstas.replace(pakeisti1, pakeisti2)
    
#     def kiek_ko (self):
#         zodziu_skaicius = len(self.tekstas.split())
#         didziosios = 0
#         mazosios = 0
#         skaiciai = 0
#         for char in self.tekstas:
#             if char.isupper():
#                 didziosios +=1        
#             if char.islower():
#                 mazosios +=1
#             if char.isdigit():
#                 skaiciai +=1
#         print(f"zodziu skaicius: ", zodziu_skaicius)
#         print(f"didziuju raidziu: ", didziosios)
#         print(f"mazuju raidziu: ", mazosios)
#         print(f"skaiciu: ", skaiciai)

# # sakinys1 = sakinys(input("Iveskite teksta: "))
# sakinys1 = sakinys("Siandien grazus grazus ORAS 999")

# # print(sakinys1.atbulai())
# # print(sakinys1.tekstas_mazosiomis())
# # print(sakinys1.tesktas_didziosiomis())
# # print(sakinys1.eiles_nr(3))
# # print(sakinys1.paieska("grazus"))
# # print(sakinys1.pakeistas("Siandien","Rytoj"))
# # print(sakinys1.kiek_ko())



                                  ###############   UZDUOTIS NR.2

# from datetime import datetime, timedelta
# class Sukaktis:
#    def __init__(self, metai, menuo, diena):
#        self.data = datetime(metai, menuo, diena)
#    def kiek_laiko_praejo(self):
#        dabar = datetime.now()
#        skirtumas = dabar - self.data
#        metai = skirtumas.days // 365
#        savaites = skirtumas.days // 7
#        dienos = skirtumas.days
#        valandos = skirtumas.seconds // 3600
#        minutes = skirtumas.seconds // 60
#        sekundes = skirtumas.seconds
#        return {"metai": metai,"savaites": savaites,"dienos": dienos,"valandos": valandos,"minutes": minutes,"sekundes": sekundes}
#    def ar_keliamieji_metai(self):
#        metai = self.data.year
#        return "keliamieji" if metai % 4 == 0 and (metai % 100 != 0 or metai % 400 == 0) else "nekeliamieji"
#    def atimti_dienas(self, dienos):
#        nauja_data = self.data - timedelta(dienos)
#        return nauja_data
#    def prideti_dienas(self, dienos):
#        nauja_data = self.data + timedelta(dienos)
#        return nauja_data

# sukaktis = Sukaktis(2015,9,27)
# print(sukaktis.kiek_laiko_praejo())
# # print(sukaktis.ar_keliamieji_metai())
# # print(sukaktis.atimti_dienas(789))
# # print(sukaktis.prideti_dienas(123))


                                    ############### UZDUOTIS NR.3



# class sakinys:
#     def __init__(self, tekstas="Siandien grazus grazus ORAS 999"):
#         self.tekstas = tekstas            
        
#     def __str__(self):
#         return self.tekstas

#     def atbulai(self):
#         return f"{self.tekstas[::-1]}"
#     def tekstas_mazosiomis(self):
#         return f"{self.tekstas.casefold()}"
#     def tesktas_didziosiomis(self):
#         return f"{self.tekstas.upper()}"
#     def eiles_nr(self, pagal_numeri):
#         pagal_numeri1 = (self.tekstas.split())
#         return pagal_numeri1[pagal_numeri]   
#     def paieska(self, surasti):
#         surasti = self.tekstas.count(surasti)
#         return surasti
#     def pakeistas(self, pakeisti1, pakeisti2):
#         padalintas = (self.tekstas)
#         padalintas[pakeisti1] = pakeisti2
#         return padalintas
    
#     def kiek_ko (self):
#         zodziu_skaicius = len(self.tekstas.split())
#         didziosios = 0
#         mazosios = 0
#         skaiciai = 0
#         for char in self.tekstas:
#             if char.isupper():
#                 didziosios +=1        
#             if char.islower():
#                 mazosios +=1
#             if char.isdigit():
#                 skaiciai +=1
#         print(f"zodziu skaicius: ", zodziu_skaicius)
#         print(f"didziuju raidziu: ", didziosios)
#         print(f"mazuju raidziu: ", mazosios)
#         print(f"skaiciu: ", skaiciai)

# # sakinys1 = sakinys(input("Iveskite teksta: "))
# # sakinys1 = sakinys("Siandien grazus grazus ORAS 999")
# sakinys1 = sakinys()
# print(sakinys1)
# # print(sakinys1.atbulai())
# # print(sakinys1.tekstas_mazosiomis())
# # print(sakinys1.tesktas_didziosiomis())
# # print(sakinys1.eiles_nr(3))
# # print(sakinys1.paieska("grazus"))
# # print(sakinys1.pakeistas("Siandien","Rytoj"))
# # print(sakinys1.kiek_ko())


#$$%^%$^#^@$^$^#$^#^$#$^@#%^@#%@#%^@#


# from datetime import datetime, timedelta
# class Sukaktis:
#     def __init__(self, metai=1996, menuo=4, diena=23):
#         self.data = datetime(metai, menuo, diena)
#     def kiek_laiko_praejo(self):
#         dabar = datetime.now()
#         skirtumas = dabar - self.data
#         metai = skirtumas.days // 365
#         savaites = skirtumas.days // 7
#         dienos = skirtumas.days
#         valandos = skirtumas.seconds // 3600
#         minutes = skirtumas.seconds // 60
#         sekundes = skirtumas.seconds
#         return {"metai": metai,"savaites": savaites,"dienos": dienos,"valandos": valandos,"minutes": minutes,"sekundes": sekundes}
#     def ar_keliamieji_metai(self):
#         metai = self.data.year
#         return "keliamieji" if metai % 4 == 0 and (metai % 100 != 0 or metai % 400 == 0) else "nekeliamieji"
#     def atimti_dienas(self, dienos):
#         nauja_data = self.data - timedelta(dienos)
#         return nauja_data
#     def prideti_dienas(self, dienos):
#        nauja_data = self.data + timedelta(dienos)
#        return nauja_data
#     def __str__(self):
#         return self.data.strftime("%Y-%m-%d")
   
# sukaktis = Sukaktis()
# print(sukaktis)
# # print(sukaktis.kiek_laiko_praejo())
# # print(sukaktis.ar_keliamieji_metai())
# # print(sukaktis.atimti_dienas(7890))
# # print(sukaktis.prideti_dienas(12345))




######################################### UZDUOTIS NR.4


# class sakinys:
#     def __init__(self, tekstas):
#         self.tekstas = tekstas            
        

#     def atbulai(self):
#         return f"{self.tekstas[::-1]}"
#     def tekstas_mazosiomis(self):
#         return f"{self.tekstas.casefold()}"
#     def tesktas_didziosiomis(self):
#         return f"{self.tekstas.upper()}"
#     def eiles_nr(self, pagal_numeri=5):
#         padalintas = (self.tekstas.split())
#         if pagal_numeri ==5:
#             return(self.tekstas)
#         if pagal_numeri == 0:
#             return(padalintas[0])
#         if pagal_numeri == 1:
#             return(padalintas[1])
#         if pagal_numeri == 2:
#             return(padalintas[2])
#         if pagal_numeri == 3:
#             return(padalintas[3])
#         if pagal_numeri == 4:
#             return(padalintas[4])    
            
#     def paieska(self, surasti):
#         surasti = self.tekstas.count(surasti)
#         return surasti
#     def pakeistas(self, pakeisti1, pakeisti2):
#         return self.tekstas.replace(pakeisti1, pakeisti2)
    
#     def kiek_ko (self):
#         zodziu_skaicius = len(self.tekstas.split())
#         didziosios = 0
#         mazosios = 0
#         skaiciai = 0
#         for char in self.tekstas:
#             if char.isupper():
#                 didziosios +=1        
#             if char.islower():
#                 mazosios +=1
#             if char.isdigit():
#                 skaiciai +=1
#         print(f"zodziu skaicius: ", zodziu_skaicius)
#         print(f"didziuju raidziu: ", didziosios)
#         print(f"mazuju raidziu: ", mazosios)
#         print(f"skaiciu: ", skaiciai)

#     def __str__ (self):
#         return(self.tekstas)

# sakinys1 = sakinys("Siandien grazus grazus ORAS 999")

# print(sakinys1)
# # print(sakinys1.atbulai())
# # print(sakinys1.tekstas_mazosiomis())
# # print(sakinys1.tesktas_didziosiomis())
# # print(sakinys1.eiles_nr())
# # print(sakinys1.paieska("grazus"))
# # print(sakinys1.pakeistas("Siandien","Rytoj"))
# # print(sakinys1.kiek_ko())




#%$#^%$^%%&^%^&%&^%&%&*^*&




# from datetime import datetime, timedelta
# class Sukaktis:
#     def __init__(self, metai, menuo, diena):
#         self.data = datetime(metai, menuo, diena)
#     def kiek_laiko_praejo(self):
#         dabar = datetime.now()
#         skirtumas = dabar - self.data
#         metai = skirtumas.days // 365
#         savaites = skirtumas.days // 7
#         dienos = skirtumas.days
#         valandos = skirtumas.seconds // 3600
#         minutes = skirtumas.seconds // 60
#         sekundes = skirtumas.seconds
#         return {"metai": metai,"savaites": savaites,"dienos": dienos,"valandos": valandos,"minutes": minutes,"sekundes": sekundes}
#     def ar_keliamieji_metai(self):
#         metai = self.data.year
#         return "keliamieji" if metai % 4 == 0 and (metai % 100 != 0 or metai % 400 == 0) else "nekeliamieji"
#     def atimti_dienas(self, dienos):
#         nauja_data = self.data - timedelta(dienos)
#         return nauja_data
#     def prideti_dienas(self, dienos):
#         nauja_data = self.data + timedelta(dienos)
#         return nauja_data
        
#     def __str__(self):
#         return self.data.strftime("%Y-%m-%d")
   
# sukaktis = Sukaktis(2015,9,27)
# print(sukaktis)
# # print(sukaktis.kiek_laiko_praejo())
# # print(sukaktis.ar_keliamieji_metai())
# # print(sukaktis.atimti_dienas(789))
# # print(sukaktis.prideti_dienas(123))





######################################### UZDUOTIS NR.5





# class Irasas:
#     def __init__(self, pajamos, islaidos):
#         self.pajamos = pajamos
#         self.islaidos = islaidos


# pajamos_visos = []
# Visos_pajamos = 0
# for skaicius in pajamos_visos:
#     Visos_pajamos += skaicius
#     print(Visos_pajamos)
# islaidos_visos = []
# Visos_islaidos = 0
# for skaiciuss in islaidos_visos:
#     Visos_islaidos += skaiciuss

# while True:
#     pasirinkimas = int(input("Pasirinkite:\n1 - įvesti pajamas\n2 - įvesti išlaidas\n3 - pajamau, islaidu balansas\n"))
#     if pasirinkimas == 1:
#         pajamos = int(input("Įveskite pajamas: "))
#         pajamos1 = pajamos
#         pajamos_visos.append(pajamos1)
#     if pasirinkimas == 2:
#         islaidos = int(input("Įveskite islaidas: "))
#         islaidos1 = islaidos                                                      
#         islaidos_visos.append(islaidos1)                                                                   
#     if pasirinkimas == 3:
#         print(f"Visos pajamos: {Visos_pajamos}")
#         print(f"Visos islaidos: {Visos_islaidos}")
#     if pasirinkimas == 4:
#         print(f"Visos pajamos: {pajamos_visos}")
#         print(f"Visos islaidos: {islaidos_visos}")
#         break
#     if pasirinkimas == 5:
#         print()
#         break

###########################################################

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















"""

class sakinys:
    def __init__(self, tekstas):
        self.tekstas = tekstas            
    
    def atbulai(self):
        return f"{self.tekstas[::-1]}"
    def tekstas_mazosiomis(self):
        return f"{self.tekstas.casefold()}"
    def tesktas_didziosiomis(self):
        return f"{self.tekstas.upper()}"
    
    # def __int__(self):
    #     self.tekstas.split()
    #     return f"{self.tekstas}"

    def kiek_ko (self):
        zodziu_skaicius = len(self.tekstas.split())
        didziosios = 0
        mazosios = 0
        skaiciai = 0
        for char in self.tekstas:
            if char.isupper():
                didziosios +=1        
            if char.islower():
                mazosios +=1
            if char.isdigit():
                skaiciai +=1
        print(f"zodziu skaicius: ", zodziu_skaicius)
        print(f"didziuju raidziu: ", didziosios)
        print(f"mazuju raidziu: ", mazosios)
        print(f"skaiciu: ", skaiciai)

tekstas1 = sakinys(input("Iveskite teksta: "))
# tekstas2 = sakinys("Siandien grazus oras")


print(tekstas1.atbulai())
print(tekstas1.tekstas_mazosiomis())
print(tekstas1.tesktas_didziosiomis())
print(tekstas1.kiek_ko())


# print(tekstas2)


"""