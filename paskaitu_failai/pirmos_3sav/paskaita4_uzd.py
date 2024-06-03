# ﻿﻿﻿Grazinti triju paduoty skaiciu suma.
# ﻿﻿﻿Grazintu paduoto saraso is skaiciu, suma.
# ﻿﻿﻿Atspausdintu didziausia is keliu paduotu skaiciu (panaudojant *args).
# ﻿﻿﻿Grazintu paduota stringa atbulai.
# ﻿﻿﻿Atspausdintu, kiek paduotame stringe yra Zodziu, didziuju ir mazuju raidziu, skaiciu.
# ﻿﻿﻿Grazintu sarasa tik su unikaliais paduoto saraso elementais.
# ﻿﻿﻿Grazintu, ar paduotas skaicius yra pirminis.
# ﻿﻿﻿Isrikiuotu paduoto stringo Zodius nuo paskutinio iki pirmojo
# ﻿﻿﻿Grazina, ar paduoti metai yra keliamieji, ar ne.
# ﻿﻿﻿﻿Atspausdina, kiek nuo paduotos sukakties praéjo metu, mènesiu, dienu, valandu, minuciu, sekundziu.

# darbuotojas = Darbuotojas("Petras", 11, "2024-04-21")       
# print(f"{darbuotojas.vardas} atlyginimas: {darbuotojas.paskaiciuoti_atlyginima()} EUR")

# normalus_darbuotojas = NormalusDarbuotojas("Sigis", 9, "2024-04-21")
# print(f"{normalus_darbuotojas.vardas} atlyginimas: {normalus_darbuotojas.paskaiciuoti_atlyginima()} EUR")

                                                            #1
                                                
# def pliusavimas( skaicius1, skaicius2, skaicius3):
#     suma = skaicius1 + skaicius2 + skaicius3 
#     return suma


# # ---------------

# skaicius1 = float(input("iveskite pirma skaiciu: "))  
# skaicius2 = float(input("iveskite antra skaiciu: "))  
# skaicius3 = float(input("iveskite trecia skaiciu: "))  
# rezultatas = pliusavimas( skaicius1, skaicius2, skaicius3)
# print(("rezultatas yra: "), rezultatas )              

                                                            #2
# Grazintu paduoto saraso is skaiciu, suma.


# sarasas = [7,3,6,4,5,5,70]
# bendra_suma = 0
# for suma in sarasas:
#     bendra_suma += suma
# print(bendra_suma)

                                                            #3


# Atspausdintu didziausia is keliu paduotu skaiciu (panaudojant *args).

# def didz_skaicius(*args):
#     for skaiciai in args:
#         print()
# def maximum(*args):
#      return max(args)
# didz_skaicius(1,2,3,4,5,6,91,7,8,9,999)
# didziausias = maximum(1,2,3,4,5,6,91,7,8,9,999)
# print(didziausias)

                                                            #4


#Grazintu paduota stringa atbulai.

# zodis = "laisvalaikis"
# print(zodis[::-1])



                                                            #5
# Atspausdintu, kiek paduotame stringe yra Zodziu, didziuju ir mazuju raidziu, skaiciu.
                                                        

# def sakinio_komponentai(tekstas):
#     zodziu_skaicius = len(tekstas.split())
#     didziosios = 0
#     mazosios = 0
#     skaiciai = 0
#     for char in tekstas:
#         if char.isupper():
#             didziosios +=1         #didziosios = didziosio + 1
#         if char.islower():
#             mazosios +=1
#         if char.isdigit():
#             skaiciai +=1


#     print(f"zodziu skaicius: ", zodziu_skaicius)
#     print(f"didziuju raidziu: ", didziosios)
#     print(f"mazuju raidziu: ", mazosios)
#     print(f"skaiciu: ", skaiciai)
# sakinys = input("iveskite sakini: ")
# sakinio_komponentai(sakinys)





                                                           #6


#Grazintu sarasa tik su unikaliais paduoto saraso elementais.


# def unikalus_sarasas(sarasas):
#     return list(set(sarasas))
 
# sarasas = [1, 2, 3, 3, 4, 5, 5,]
# unikalus_sarasas = unikalus_sarasas(sarasas)
 
# print(unikalus_sarasas)




                                                            #7



# def pirminis_skaicius (skaicius):
#     if skaicius / skaicius or skaicius




                                                            #8





# Isrikiuotu paduoto stringo Zodius nuo paskutinio iki pirmojo

# def reverse_order(sakinys):
#     return ' '.join(sakinys.split(' ')[::-1])
 
# user_input = input("iveskite teksta: ")
# print(reverse_order(user_input))





                                                      #9
# Grazina, ar paduoti metai yra keliamieji, ar ne.      

# paduoti_metai = int(input("Iveskite metus: "))
# keliameji = [lambda i=metai: i for metai in (paduoti_metai) if 
#              (metai % 400 == 0) or (metai % 100 != 0 and metai % 4 == 0)]
# for vienas in keliameji:
#     print(vienas())









                                                            #10
# Atspausdina, kiek nuo paduotos sukakties praéjo metu, mènesiu, dienu, valandu, minuciu, sekundziu.
import datetime

#                                             #       2004-9-9 23:45:00

# ivesta_data = input("Iveskite data: ")
# data2 = datetime.datetime.strptime(ivesta_data, "%Y-%m-%d %H:%M:%S")
# skirtumas = (datetime.datetime.now() - data2)
# skirtumas.total_seconds

# print("Metu praejo: ",(round(skirtumas.days // 365)) )
# print("Menesiu praejo: ",(round(skirtumas.total_seconds() / 2592000)) )
# print("Dienu praejo: ",(round(skirtumas.total_seconds() / 86400)))
# print("Valandu praejo: ",(round(skirtumas.total_seconds() / 3600)))
# print("Minuciu praejo: ",(round(skirtumas.total_seconds() / 60)))
# print("Sekundziu praejo: ",(round(skirtumas.total_seconds())))
