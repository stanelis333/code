import numpy
import datetime
import pandas




# dict_one = {'a': 10, 'b': 20, 'c': 30}
# dict_two = {'b': 200, 'd': 400}
# dict_one .update(dict_two )
# print(dict_one )




#########################




# skaicius = int(input("iveskite skaicu: "))
# if skaicius > 0: 
#     print("True")
# elif skaicius <= 0:
#     print("False")



# skaicius = int(input("Iveskite skaiciu "))
# ar_skaicius_teigiamas = bool() # NEBUTINAS
# if skaicius > 0:
#     ar_skaicius_teigiamas = True
# else:
#     ar_skaicius_teigiamas = False
# print(ar_skaicius_teigiamas)






#################

# siandien = datetime.datetime.today()
# print(siandien)

# siandien = datetime.date.today()
# print(siandien)

# siandien = datetime.datetime(2099,9,23,17,45,30)
# print(siandien)


# print(datetime.date.today().strftime("%j"))


# data = datetime.datetime(2022,10,15, 10,15,10)
# print(data - datetime.timedelta(days=30))
# print(data + datetime.timedelta(hours=30))
# print(data + datetime.timedelta(hours=30, days=3))


                                            ###################


# ivesta_data = input("Iveskite data: ")
# gimimo_data = datetime.datetime.strptime(ivesta_data, "%Y-%m-%d")
# print("Jusu gimimo data yra: ", gimimo_data)
# skirtumas = (datetime.datetime.now() - gimimo_data)
# print("Jums yra: ",skirtumas.days / 365) 


                                                ###################



# print(datetime.datetime.now())
# data = (datetime.datetime.now())
# print(data - datetime.timedelta(days=5))
# print(data + datetime.timedelta(hours=8))
# print(data.strftime("%Y %m %d, %H:%M:%S"))

# ivesta_data = input("Iveskite gimimo data: ")
# gimimo_data = datetime.datetime.strptime(ivesta_data, "%Y-%m-%d")

                                        #############        #########

#                       1996-04-23 8:30:15

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


                                ###################################




# try:
#     # 7 / 0
#     # int("Hello")
#     "labas" - 5
#     open("Neegzistuojantis.txt")
#     print(7/1)
# except ZeroDivisionError:
#     print("Dalyba is nulio negalima")
#     print()
#     print()
#     print()
#     print()
#     print()
# except ValueError:
#     print("Pateikta netinkama reiksme")
# except TypeError:
#     print("Neteisingas tipas")
# except:
#     print("Nenumatyta klaida")
 
# print("Labas")


                                            ###################

# while True:
#     try:
#         x = int(input("Iveskite skaiciu: "))
#         break
#     except ValueError:
#         print("Ivedete ne skaiciu. Bandykite dar karta")
        



# sarasas = [5, 8, "Lietuva", 95, "zodis", True]
# suma = 0
# for x in sarasas:
#     if type (x) is int:
#         suma += x
# print(suma)









# sarasas = ["Vienas", "Du", "Trys"]
# skaicius = 123
# kablelis = 5.56
# zodynas = {"Mantas": 20}
# loginis = True
# print(type(sarasas))
# print(type(skaicius))
# print(type(kablelis))
# print(type(zodynas))
# print(type(loginis))

        