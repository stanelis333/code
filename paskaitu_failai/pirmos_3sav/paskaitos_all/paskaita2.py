import numpy
import random

# print("hello")


# organization_Name = "Microsoft"
# est_year = 1985

# print('-'*45)
# print(f'|    organization_Name  |\test_Year    |')
# print('-'*45)
# print(f'|\t{organization_Name}\t|\t{est_year}\t    |')
# print('-'*45)
# print(f'|\t{organization_Name}\t|\t{est_year}\t    |')
# print('-'*45)
# print(f'|\t{organization_Name}\t|\t{est_year}\t    |')
# print('-'*45)


# rezultatas = (8==8) or (7==7)
# print(rezultatas)

# rezultatas = (8!=9) and (6!=7)
# print(rezultatas)



# amzius = float(input("iveskite savo amziu: "))
# if amzius < 20:
#     print("negalite isigyti alkoholio.")
# if amzius >= 20:
#     print("galite isigyti alkoholio.")
# if amzius > 80:
#     print("bet ar jums tikrai to reikia?")




# amzius = float(input("iveskite savo amziu: "))
# if amzius >= 20:
#     print('Jus galite isigyti alkoholio')
# else:
#     print('Jus negalite isigyti alkoholio')



# amzius = int(input('Iveskite savo amziu: '))
# if amzius >= 20:
#     print('Jus galite isigyti alkoholio')
# elif amzius < 20:
#     print("jusu amzius per mazas")
# else:
#     print('Jus negalite isigyti alkoholio')





# while True:
#     try:
#         slaptazodis = int(input('Iveskite slaptazodi: '))
#         break     
#     except ValueError:
#         print("Įvedėte ne skaičių. Bandykite dar kartą")
    

    # match slaptazodis:
    #     case 55555:
    #         print("slaptazodis yra teisingas ")
    # if slaptazodis != 55555:
    #     print("bandykite dar karta")
        


    
    

# skaicius1 = int(input("Iveskite pirma skaiciu: ")) 
# skaicius2 = int(input("iveskite antra skaiciu: "))

# if skaicius1 > skaicius2:
#     print(skaicius1, ">", skaicius2)
# elif skaicius1 == skaicius2:
#     print(skaicius1, "=", skaicius2)
# else: 
#     print(skaicius1, "<", skaicius2)

                                            #######################################################################################


# kodas = (input("Iveskite koda: "))
# kodas = ("zen of pyTHon")
#                     # # match kodas:
#                     # #     case ("zen of python"):
# print(kodas[5])
# print(kodas[-6])
# print(kodas[0:3])
# print(kodas[7:13])
# print(kodas[::-1])
# print(kodas.split())
# print(kodas.replace('pyTHon', 'programming'))
# print(kodas.upper())
# print(kodas.casefold())
# print(kodas.capitalize())
# print(kodas.count('o'))
# print(kodas.find ('H'))


# skaicius1 = str(input("iveskite pirma skaiciu: "))
# skaicius2 = str(input)
# str(input("Ar norite paskaiciuoti perimetrus ir plotus?  "))                            

# a2 = float(input("iveskite krastine: "))
# b2 = float(input("iveskite sekancia krastine: "))
# perimetras = (a2 + b2) * 2 
# plotas = a2 * b2 
# print(("perimetras yra:"), perimetras)
# print(("plotas yra:"), plotas)


# skaiciai = [3,7,9]
# skaiciai.append (15)
# skaiciai.extend(skaiciai)
# skaiciai[7] = 1
# #skaiciai.pop(9)==ismeta skaiciu
# print(skaiciai)



# zodis = "namas"
# print(len(zodis))

# skaiciai = [8,6,7,9]
# print(skaiciai[-1])   

# pazymiai = {"jusiatas": [7,5,9], "paulius":[1,4,9], "karolis": [9,5,9]}
# print(pazymiai)        


# kompanijos = {"Codeacademy":["Justas", "Paulius", "Edvinas"], "Maxima": ["Arturas", "Jonas"]}
# print(kompanijos["Maxima"])
# kompanijos["Norfa"] = ["Laura", "Tomas"]
# print(kompanijos)
# kompanijos["Norfa"].append("Darius")
# print(kompanijos)



# for skaicius in range(11):
#     print(skaicius)

# limitas = 100
# i = 1
# while i < limitas:
#     print(i)
#     i +=1

# for skaicius in range (10):
#     print(skaicius)


# pazymiai = {"Justas": [7,5,9], "Paulius":[1,4,9], "Karolis": [9,5,9]}
# print(pazymiai)
 
# print(("Paulius: "), (pazymiai ["Paulius"]))
# print(("Justas: "), (pazymiai ["Justas"]))
# print(("Karolis: "), (pazymiai ["Karolis"]))



# gerimai = {"gazuoti":["coca-cola", "sprite", "fanta"], "negazuoti": ["elmenhorster", "cappy"]}
# print(gerimai["gazuoti"])
# gerimai["tirsti"] = ["pomidoru sultys", "kubush"]
# print(gerimai)
# gerimai["negazuoti"].append("alloe vera")
# print(gerimai["negazuoti"])
# gerimai["negazuoti"].remove("cappy")
# print(gerimai["negazuoti"])
# gerimai["gazuoti"] = ("sprite", "coca-cola")
# print(gerimai)

# skaicius = float(input("iveskite skaiciu: "))
# while skaicius > 0:
#     print(float(input("iveskite skaiciu: ")))
# if skaicius < 0:
#     print(skaicius)


#     float(input("iveskite dar viena skaiciu: "))
 
# elif skaicius < 0:
#     print("1,2,3,4,5,6,7,8,9")


# zodis = int(5.45)
# print(zodis)
# zodis = str(5.45)
# print(zodis+zodis)
# zodis = float(5.45)
# print(zodis+zodis)



# zodis = "labas kaip sekasi"
# print(zodis.count('a'))
# zodis = "labas kaip sekasi"
# print(zodis.split())



# pinigai = float(input("Kiek turite pinigu? "))

# if pinigai >= 500 and pinigai < 1500:
#     print("dar pinigu pakanka")
# elif pinigai > 1500 and pinigai < 5000:
#     print("turi daug pinigu")
# elif pinigai > 5000 and pinigai < 99999999999:
#     print("tu esi turtingas")
# else:
#     print ("tau truksta pinigu")





# skaicius1 = 5
# skaicius2 = 8
# skaicius3 = 15
# skaiciai = [skaicius1,skaicius2,skaicius3,999]

# # print(skaiciai)
# # print(skaiciai.index(8))   
# # print(skaiciai[2])
# # skaiciai.append(111)
# # skaiciai.remove(5)
# # skaiciai.pop(3)
# skaiciai[3] = 888
# print(skaiciai)



# amziai = {"Vaidas":5, "Arnas":15, "Karolina": 25}
# print(amziai['Vaidas'])
# print(amziai['Arnas'])
# print(amziai['Karolina'])


# greiciai = {1:7, 2:7.15, 3:8}
# print(greiciai[2])
# greiciai[4] = 8.2
# print(greiciai)
# greiciai[1] = 6.9
# print(greiciai)
# del greiciai[4]
# print(greiciai)





# suma = 0
# kiekis = int(input("Iveskite skaiciu: "))
# for skaicius in range(kiekis):
#     suma = suma + skaicius
# print(suma)



# suma = 0
# kiekis = int(input("Iveskite kieki "))
# for skaicius in range(kiekis): # if skaicius < 10: suma = suma + skaicius
#     print(skaicius)
#     if (skaicius % 2) == 0:
#         suma += skaicius # suma = suma + skaicius
# print(suma)


# suma = 0
# skaiciai = [5,7,9,1,5,4]
# for skaicius in skaiciai: # if skaicius < 10: suma = suma + skaicius
#     # print(skaicius)
#     if (skaicius % 2) == 0:
#         suma += skaicius # suma = suma + skaicius
# print(suma)




# amziai = {"Arnas":10, "Vaidas":15, "Karolina":25}
# for amzius in amziai.items():
#     print(amzius)
# for amzius in amziai.keys():
#     print(amzius)
# for amzius in amziai.values():
#     print(amzius)


                    ##############################################################################
                                    #    WHILE


# kiekis = 0
# while 10>kiekis:
#     print("labas")
#     kiekis = kiekis + 1



# kiekis = 0
# while 10>3:
#     print("labas")
#     if input("Iveskite zodi: ") == '':
#         break


# kiekis = 0
# kiekis_vid = 0
# while kiekis < 10:
#     print("Isorinio ciklo kiekis: ", kiekis)
#     while kiekis_vid < 5:
#         print(f"Vidinio ciklo kiekis: {kiekis_vid}")
#         kiekis_vid += 1
#     kiekis = kiekis + 1
#     kiekis_vid = 0



# kiekis_vid = 0
# while kiekis < 10:
#     print("Isorinio ciklo kiekis: ", kiekis)
#     while kiekis_vid < 5:
#         print(f"Vidinio ciklo kiekis: {kiekis_vid}")
#         kiekis_vid += 1
#         if kiekis_vid == 3:
#             break
#     kiekis = kiekis + 1
#     kiekis_vid = 0


# skaiciai = [5,7,9,1,5,4]
# kiekis = 0
# while kiekis < len(skaiciai):
#     print(skaiciai[kiekis])
#     kiekis += 1

######################################################

# my_list = [1, 2, 3]
# # print(4 in my_list)

# my_list = [50, 99, 1, -50]
# print(max(my_list))

########################################################




# user = "Johnny"
# privileged_users = ["Tom", "Albert", "Stephen"]
# if user in privileged_users:
#     print(f"Welcome home {user}")
# else:
#     print("INTRUDER ALLERT. Silently calling police...")


# dict_one = {'a': 10, 'b': 20, 'c': 30}
# dict_two = {'b': 200, 'd': 400}
# dict_one .update(dict_two )
# print(dict_one )
