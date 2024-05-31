



# class Automobilis:
#    def __init__ (self, marke, modelis):
#       self.marke = marke
#       self.modelis = modelis
#    # def __str__ (self):
#    #    return f"{self.marke} {self.modelis}"
   
# # automobiliai = [Automobilis("Toyota", "Avensis"), Automobilis("Toyota", "Corolla"), Automobilis("Toyota", "Camry")]

# # with open("automobilis.pkl", "wb") as failas:
# #    pickle.dump(automobiliai, failas)

# with open("automobilis.pkl", "rb") as failas:
#    automobiliai1 = pickle.load(failas)
#    for automobilis in automobiliai1:
#       # print("Marke", automobilis.marke)
#       print(automobilis.modelis)
#       # print(automobilis)


# with open ("C:\code\BibliotekosValdymas\duomenys\knygu_sarasas.pkl", "rb") as pateikti:
#     pateiktis = pickle.load(pateikti)
#     for autorius in pateiktis:
#       print("Marke", autorius.marke)
#       print("Modelis", autorius.modelis)

   #  print(pateiktis)








#sarasas

# sarasas = []
# skaiciai = [4, 5, 45, 95]
# zodziai = ["Labas ", "vakaras ", "Lietuva"]
# visko_po_truputi = [5, 5.6, "Lietuva", [5, 6, 15], True]
# print(skaiciai[1])
# print(zodziai[1])
# print(visko_po_truputi[1])
# print(skaiciai)
# for skaiciai_i_apacia in skaiciai:
#     print(skaiciai_i_apacia)
# suma = 0
# for skaiciu_suma in skaiciai:
#     suma += skaiciu_suma
# print(suma)



# skaiciai = [2, 6, 7, 9, 41, 4, 46, 789,84994]

# skaiciu_suma = 0

# for skaicius in skaiciai:
#     skaiciu_suma += skaicius 

# print(skaiciu_suma)

# zodynas 

# amzius = {"Sarunas" : 28, "Arnas" : 19, "Antanas" : 80 }
# print(amzius["Antanas"])
# print(amzius["Sarunas"])

# amzius["Nerius"] = 32

# print(amzius)


# def sudetis(skaicius1, skaicius2):
#     return skaicius1 + skaicius2
# def daugyba(skaicius1, skaicius2):
#     return skaicius1 * skaicius2
# def dalyba(skaicius1, skaicius2):
#     return skaicius1 // skaicius2

# ivestis1 = float(input("iveskite skaiciu: "))
# ivestis2 = float(input("iveskite antra skaiciu: "))

# print("suma: ",sudetis(ivestis1,ivestis2))
# print("sudauginus: ", daugyba(ivestis1,ivestis2))
# print("padalinus: ", dalyba(ivestis1,ivestis2))


# def didziosiom(tekstas):
#     return tekstas.upper()
# def mazosios(tekstas):
#     return tekstas.lower()
# ivestis = input("Iveskite teksta: ")
# print(didziosiom(ivestis))
# print(mazosios(ivestis))




#############################

# class automobiliai:
#     def __init__(self, marke, modelis, metai, kuro_sanaudos):
#         self.marke = marke
#         self.modelis = modelis
#         self.metai = metai
#         self.kuro_sanaudos = kuro_sanaudos


#     def __str__(self):
#         return f"marke:  {self.marke}\nmodelis:  {self.modelis}\nmetai:  {self.metai}\nKuro sanaudos:  {self.kuro_sanaudos}"
    
# auto1 = automobiliai("toyota","prius", 2004, "100km/4.9L")
# auto2 = automobiliai("audi","a4", 1996, "100km/4.7L")
# auto3 = automobiliai("bmw","320", 2013, "100km/5.5L")

# print(auto1)
# # print(auto2)
# # print(auto3)

# # automobilis = []
# # automobilis.append(auto1)
# # automobilis.append(auto2)
# # automobilis.append(auto3)

# # for automobiliai in automobilis:
# #     print(automobiliai.marke, automobiliai.modelis , automobiliai.metai, automobiliai.kuro_sanaudos)


############################




# class Kate:
#     def __init__(self, vardas, amzius, spalva="juoda"):
#         # Savybės:
#         self.vardas = vardas
#         self.amzius = amzius
#         self.spalva = spalva

#     # Metodas:
#     def miaukseti(self, miauksejimas="Miau\n", kartai=3):
#         return f"Katė vardu {self.vardas} \n{miauksejimas * kartai}"

#     def __str__(self):
#         return f"Katė vardu {self.vardas}   amzius: {self.amzius}   Spalva: {self.spalva}, miauksejimas * kartai"

#     # def _repr_(self):
#     #     return f"Kate vardu {self.vardas}"

# kate1 = Kate("Nila", 13, "Pilka")
# # print(kate1)
# print(kate1.miaukseti())


##################################################################################################################################
# import pickle
# kates = []
# while True:
#     pasirinkimas = input("Pasirinkite:\n1 - įvesti katę\n2 - peržiūrėti visas kates\n3 - išeiti iš programos\n")
#     if pasirinkimas == "1":
#         vardas = input("Įveskite katės vardą: ")
#         amzius = input("Įveskite katės amžių: ")
#         spalva = input("Įveskite katės spalvą: ")
#         kate = f"Vardas: {vardas}| Amzius: {amzius}| Spalva: {spalva}"
#         kates.append(kate)
#         with open ("kates.pkl", "ab") as kt:
#          pickle.dump(kt)
#     if pasirinkimas == "2":
#         for kate in kates:
#             print(kate)
#     if pasirinkimas == "3":
#         print("Viso gero")
#         break

        


##################################################################################################################################


# def kvadratu(*skaiciai):
#     for skaicius in skaiciai:
#         print(skaicius **2)

# kvadratu(8)

# suma = 0
# def skaicius_suma(*skaiciai):
#     for skaicius in skaiciai:
#         print(skaicius)

# skaicius_suma(87,13)

########################################

# sarasas = [5, 8, "Lietuva", 95, "Žodis", True]

# suma = 0

# for x in sarasas:
#     if type(x) is int:
#         suma += x

# print(suma)

#############################


# try:
#     skaicius = int(input("Įveskite skaičių: "))
# except:
#     print("Įvestas klaidingas skaičius")


###

# while True:
#     try:
#         Xx = int(input("Įveskite skaičių: "))
#         break
#     except ValueError:
#         print("Įvedėte ne skaičių. Bandykite dar kartą")

# print(Xx)


##################################


# skaiciai = [2, 600, 7, 9, 41, 4, 46, 789]
# skaiciu_suma = 0
# for skaicius in skaiciai:
#     skaiciu_suma += skaicius
# print(skaiciu_suma)

####################################################################


# class Irasas:
#    def __init__(self, tipas, suma):
#       self.tipas = tipas
#       self.suma = suma

# str_(self):
# return f"suma: {self.suma}, tipas: {self.tipas} "

# def

# def

# class Biudzetas:
# def _init_(self):
# self.zurnalas = []
# self.balansas = 0

# def prideti_pajamu_irasa(self, suma):
# irasas = Irasas("Pajamos", suma)
# self.zurnalas. append(irasas)
# self.balansas += suma

# def prideti_islaidu_irasa(self, suma):
# irasas = Irasas("Islaidos", suma)
# self.zurnalas.append(irasas)
# self.balansas -= suma

# biudzetas = Biudzetas()

# while True:
# pasirinkimas = input("Pasirinkite veiksma:\n1. Prideti pajamas\n2. Prideti islaidas\n3. Parodyti balansa\n4. Baigti\n")

# if pasirinkimas == "1":
# pajamos = int(input("Iveskite pajamas: "))
# biudzetas.prideti_pajamu_irasa(pajamos)

# elif pasirinkimas == "2":
# islaidos = int(input("Iveskite islaidas: "))
# biudzetas.prideti_islaidu_irasa(islaidos)

# elif pasirinkimas == "3":
# print(f"Balansas: {biudzetas.balansas}")

# elif pasirinkimas == "4":
# print("Programa baige darba.")
# break

# else:
# print("Netinkamas pasirinkimas. Bandykite dar karta.")


###############################################################           LENTELE

# for i in range(0,50):
#     print('-'*30)
#     print(f"{i:>{10}.5f}|{i+1:<{10}.5f}")
#     print('-'*30)

###############################################################        

# import timeit
# print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
# print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))

# ##############################################################          


# mano_tuple_sarasas = [(4,6,8),(1,7,9),(9,4,4),(5,15,8),(10,19,9)]
 
# for a,b,c in mano_tuple_sarasas: # a = mano_tuple_sarasas[0][0] b = mano_tuple_sarasas[0][1] ... a = mano_tuple_sarasas[1][0] b = mano_tuple_sarasas[1][1]...
#     print(f"{a}+{b}+{c}={sum((a,b,c))}")

# for ind, skaicius in enumerate(skaiciai):
#     print(f"skaicius {skaicius} yra {ind} sarase")

##############################################################


# sarasas1 = [4,5,6,7,8,9]
# sarasas2 = [3,2,1,5,4,5]

# for skai in zip(sarasas1,sarasas2):
#     print(skai)

###############################################################
   #                                                                  Lambda (map)

# skaiciai = [8,4,3]

# def cubed(x):
#     return x ** 3

# skaiciai_3 = map(lambda x: x ** 3,skaiciai)

# print(list(skaiciai_3))

# lambda x: x ** 3


###############################################################        Lambda  


# lambda a,b: a+b 


# tekstas = "Grazus rytas. Laukia grazi diena. Lyti neturetu"
# sakinys = tekstas.split(". ")
# for sak in sakinys:
#     mano_metodas = lambda a,b: a+b
#     print(mano_metodas(sak,"!"))




###############################################################


# tekstas = "4,8,9"

# iskirsytas = tekstas.split(',')

# print(iskirsytas)
# skaiciai_kon = []

# for x in iskirsytas:
#     tarpinis = int(x)*2
#     skaiciai_kon.append(tarpinis)

#.skaiciai_kon =. map(lambda.x :. int(x)*2,.tekstas.split(','))

# print(list(skaiciai_kon))




###############################################################         Lambda   (filter)


# sarasas = [4, 3, 2, 1]
# naujas = filter(lambda x: x > 2, sarasas)
# print(list(naujas))

# # [4, 3]

# sarasas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# naujas = filter(lambda x: x % 2 == 0, sarasas)
# print(list(naujas))

# # [2, 4, 6, 8, 10]

# import calendar

# metai = list(range(1900, 2150))
# naujas = list(filter(calendar.isleap, metai))
# print(naujas)

###############################################################     Lambda    (reduce)




# from functools import reduce

# sarasas = [4, 3, 2, 1]
# naujas = reduce(lambda x, y: x + y, sarasas)
# print(naujas)

# # 10

# from functools import reduce

# sarasas = [4, 3, 2, 1]
# naujas = reduce(lambda x, y: x * y, sarasas)
# print(naujas)

# 24

###############################################################


# class Gyvunas:
#    def __init__(self, vardas = None, spalva=None, amzius=None):
#       self.vardas = vardas
#       self.spalva = spalva
#       self.amzius = amzius
#    def str (self):
#       return self.vardas, self.spalva, self.amzius
#    def animal(self):
#       return "Laksto"

# class Suo(Gyvunas):
#    def balsas (self):
#       return "loja" 

# class Kate(Gyvunas):
#    def balsas (self):
#       return "murkia"

# dzeris = Suo("Dzeris", "juodas", 15)
# nila = Kate("Nila","pilka", 14)

# print(dzeris.str())
# print(dzeris.animal(), dzeris.balsas())

# print(nila.str())
# print(nila.animal(), nila.balsas())




################################################################

# class Vehicle():
#     def __init__(self, move_speed):
#         self.move_speed = move_speed
#     def Move(self):
#         print("I am moving")
 
# class LandVehicle(Vehicle):
#     def __init__(self, move_speed, distance_from_ground = 30):
#         super().__init__(move_speed)
#         self.distance_from_ground = distance_from_ground
 
#     def Move(self):
#         print("I am moving trough land")
 
# class Car(LandVehicle): # car -> LandVehicle -> Vehicle
#     def __init__(self, move_speed, wheel_amount = 4, distance_from_ground=30):
#         super().__init__(move_speed, distance_from_ground)
#         self.wheel_amount = wheel_amount
#     def Move(self):
#         print("I am moving trough land probably on a road")
 
 
#     def Drive(self):
#         print("I am driving")
 
 
# vehicle = Vehicle(15)
 
 
# land_veh = LandVehicle(30)
 
# my_car = Car(50)
 
# # print(f"vehicle speed is {vehicle.move_speed}")
# # print(f"land_veh speed is {land_veh.move_speed}")
# # print(f"my_car speed is {my_car.move_speed} and it has {my_car.wheel_amount} wheels")
 
# vehicles = [vehicle,land_veh,my_car]
 
# for v in vehicles:
#     if isinstance(v, LandVehicle):
#         v.Move()











