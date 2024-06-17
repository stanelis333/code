

# sarasas = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]

# int_kiekis = sum(type(c) is int for c in sarasas)
# print(int_kiekis)

# # 4

# str_kiekis = sum(type(c) is str for c in sarasas)
# print(str_kiekis)

# # 2

# sarasas = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]
# bool_kiekis = sum(type(c) is bool for c in sarasas)
# print(bool_kiekis)

# # 1

# float_kiekis = sum(type(c) is float for c in sarasas)
# print(float_kiekis )


                                                                  # # uzduotis NR.1

# # tekstas = "Grazus rytas. Laukia grazi diena. Lyti neturetu"
# # sakinys = tekstas.split(". ")
# # mano_metodas = lambda a,b: a+b
# # for sak in sakinys:
# #     print(mano_metodas(sak,"!"))


                                                       # #uzduotis NR.2

# from statistics import mean, median
# skaicius = list(range(51))
# daugyba = list(map(lambda x: x * 10 , skaicius))
# # print(daugyba)


# dalyba_is_7 = filter(lambda x: x % 7 == 0, daugyba)
# # print(list(dalyba_is_7))


# kvadratu = list(map(lambda x: x**2, skaicius))
# # print(list(kvadratu))


# # print(sum(kvadratu))
# # print(min(kvadratu))
# # print(max(kvadratu))
# # print(mean(kvadratu))
# # print(median(kvadratu))

# # isrikiuotas = sorted(kvadratu, reverse=True)
# # print(isrikiuotas)

# # kvadratu.sort(reverse=True)
# # print(kvadratu)

######################################################################


                                                       # #uzduotis NR.3
"""
Duotas sąrašas: sarasas = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]
Sukurti programą, kuri:
· Paskaičiuotų ir atspausdintų visų sąrašo skaičių sumą
· Sudėtų ir atspausdintų visus sąrašo žodžius
· Suskaičiuotų ir atspausdintų, kiek sąraše yra loginių (boolean) kintamųjų su True reikšme

Patarimai:
· Naudoti filter arba comprehension, sum, " ".join()

"""

                                                                                #1.

# sarasas = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]

# atskiri_skaiciai = filter(lambda x: type(x) in (int, float), sarasas)
# print(sum(atskiri_skaiciai))

# atskiri_skaiciai = filter(lambda x: isinstance(x,(int,float)), sarasas)
# print(sum(atskiri_skaiciai))

# skaiciai = [s for s in sarasas if type(s) == float or type(s) == int]
# y = sum(skaiciai)
# print(f'Skaiciu suma {y}')


# zodziai = filter(lambda x: type(x) == str, sarasas)
# sujungti_zodziai = " ".join(zodziai)
# print(sujungti_zodziai)


                                                                                 #2.


# class Zmogus:
#     def __init__(self, vardas, amzius):
#         self.vardas = vardas
#         self.amzius = amzius

#     # def __repr__(self):
#     #     return f"Vardas: {self.vardas} | Amzius: {self.amzius}"
#     def __str__(self):
#         return f"Vardas: {self.vardas} | Amzius: {self.amzius} "


# zmogus1 = Zmogus("Antanas", 77)
# zmogus2 = Zmogus("Andrius", 67)
# zmogus3 = Zmogus("Arvydas", 57)
# visi = (f"{zmogus1}\n{zmogus2}\n{zmogus3}")

# print(visi)
# # print(zmogus1)



######################################################################

