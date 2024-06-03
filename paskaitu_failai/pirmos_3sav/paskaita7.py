
import os

# 
# current_directory = os.getcwd()
# print ("Dabartinis katalogas:", current_directory)
# items = os.listdir(current_directory)
# print("Katalogo turinys:", items)

# with open("naujas_failas.txt", "a") as file:
#     for skaicius in range(1, 100):
#         file.write(f"{skaicius}. pridedamas textas\n")

# os.rename("naujas_failas.txt", "PVZ_failas.txt")

# os.remove("PVZ_failas.txt")

# items = os.listdir(current_directory)

# for item in items:
#     if os.path.isfile(item):
#         print(f"Failas: {item}")
#     else:
#         print(f"Aplankas: {item}")


################################################### uzduotis nr.1

# import this
zen = """Zen of Python
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!\n 
"""

import os
from datetime import datetime

# os.mkdir("Naujas_katalogas")

os.chdir("C:\\code\\Naujas_katalogas")
print(os.getcwd())

# 1.
# with open("Tekstas2.txt", "w") as failas:
#         failas.write(zen)
# 2.
# with open ("Tekstas2.txt", 'r') as failas:
#     print(failas.read())
# # with open("Tekstas2.txt", "r") as failas:
# #     for eilute in failas:
# #         print(eilute)
# 3.
# with open("Tekstas2.txt", "a") as failas:
#     data = os.stat("Tekstas2.txt").st_mtime
#     failas.write(f"{datetime.fromtimestamp(data)}\n")
# 

# 4. Sunumeruoti visas failo teksto eilutes (kiekvienos pradžioje pridėti skaičių):
 
# naujas = ""
# skaicius = 1
# with open('tekstas.txt', 'r') as failas:
#     for eilute in failas:
#         naujas += str(skaicius) + " " + eilute
#         skaicius += 1
 
# with open('tekstas.txt', 'w') as failas:
#     failas.write(naujas)


# def add_line_numbers(zen):
#    lines = zen.split('\n') 
#    numbered_lines = [f"{index +0}: {line}" for index, line in enumerate(lines)] 
#    return '\n'.join(numbered_lines) 
# numbered_zen = add_line_numbers(zen)
# with open("Tekstas2.txt", "w") as failas:
#    failas.write(numbered_zen)

# 5.
# with open("Tekstas2.txt", "r") as failas:
#     zen = failas.read()
#     zen = zen.replace("Beautiful is better than ugly", "Grazu yra geriau nei bjauru") 
# with open("Tekstas2.txt", "w", encoding="utf-8") as failas:
#     failas.write(zen)

# 6.
# with open("Tekstas2.txt", "r") as failas:
#     zen = failas.read()
#     print(zen[::-1])

# 7.
# with open("Tekstas2.txt", "r") as failas:
#     def sakinio_komponentai(tekstas):
#         zodziu_skaicius = len(tekstas.split())
#         didziosios = 0
#         mazosios = 0
#         skaiciai = 0
#         for char in zen:
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
#     sakinio_komponentai(zen)

# 8.
# with open("Tekstas2.txt", "r") as failas:
#    tekstas = failas.read()
# with open("Tekstas98.txt", "w") as failas:
#    failas.write(tekstas.upper())





   ################################################### uzduotis nr.2

# def main():
#     failo_pavadinimas = input("Įveskite failo pavadinimą: ")
#     with open(failo_pavadinimas, 'w', encoding='utf-8') as failas:
#         print("Įveskite tekstą (tuščia eilutė baigia įvedimą):")
#         while True:
#             eilute = input()
#             if eilute == "":
#                 break
#             failas.write(eilute + "\n")
#     print(f"Tekstas įrašytas į failą '{failo_pavadinimas}'")
# if __name__ == "__main__":
#     main()

  ###################################################  uzduotis nr.3

# def main():
#     katalogo_pavadinimas = input("Įveskite naujo katalogo pavadinima: ")
#     os.mkdir("C:\\Users\\stane\\OneDrive\\Pulpit\\",{katalogo_pavadinimas})



# if __name__ == "__main__":
#     main()



#     with open(katalogo_pavadinimas, 'w', encoding='utf-8') as failas:
#         print("Įveskite tekstą (tuščia eilutė baigia įvedimą):")
#         while True:
#             eilute = input()
#             if eilute == "":
#                 break
#             failas.write(eilute + "\n")
#     print(f"Tekstas įrašytas į failą '{katalogo_pavadinimas}'")
# if __name__ == "__main__":
#     main()






######################################################################################################


# import pickle
 
# while True:
#     try:
#         with open("biudzetas.pkl", "rb") as pickle_in:
#             biudzetas = pickle.load(pickle_in)
#             suma = 0
#             print("--------Įrašų sąrašas:---------")
#             for skaicius, irasas in enumerate(biudzetas):
#                 suma += irasas
#                 print(skaicius + 1, irasas)
#             print("Biudžeto balansas", suma)
#             print("-------------------------------")
#     except:
#         print("Nepavyko nuskaityti failo")
#         biudzetas = []
#     print("Norėdami išeiti palikite tuščią lauką ir spauskite ENTER")
#     irasas = input("Įveskite pajamas arba išlaidas: ")
#     if irasas == "":
#         break
#     irasas = float(irasas)
#     biudzetas.append(irasas)
 
#     try:
#         with open("biudzetas.pkl", "wb") as pickle_out:
#             pickle.dump(biudzetas, pickle_out)
#     except:
#         print("Nepavyko įrašyti failo")
 
# skaiciai = [4,8,9,5,6,-5]
 
 
# with open("naujas.pkl", "wb") as naujas:
#     pickle.dump(skaiciai,naujas)
 
 
# with open("naujas.txt", "rb") as skaitomas:
#     print(pickle.load(skaitomas))

