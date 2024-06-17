

# def pakelti_kvadratu(skaicius):
#     pakelti_kvadratu = skaicius ** 2
#     print(pakelti_kvadratu)
# pakelti_kvadratu(9)


# def pasisveikinti(vardas):
#     print(f"{vardas}")
# pasisveikinti("=========")
# pasisveikinti("=========")
# pasisveikinti("Šarūnas\U0001F600") 
# pasisveikinti("=========")  
# pasisveikinti("=========")


# def sudetis(a1, a2, a3,):
#     sudeti =  a1 + a2 + a3  
#     print(sudeti)
# sudetis(150,50,99)




# def dalyba(a1, a2,):
#     dalinti =  a1 / a2  
#     print(dalinti)
# dalyba(150,50,)




# def daugyba(skaicius1, skaicius2):
#     daugybos_res = skaicius1 * skaicius2
#     return daugybos_res
# res = daugyba(5, 3)
# res2 = daugyba(res, 3)
# print(res2)



# def sudetis(a1, a2, a3):
#     sudeti =  a1 + a2 + a3  
#     if sudeti % 2 ==0:
#         return "lyginis"
#     else:
#         return "nelyginis"
    
# sudetis(150,40,10)


# def teksto_ilgis(tekstas):
#     return len(tekstas)
# vardas = input("iveskite varda: ")
# vardo_ilgis = teksto_ilgis (vardas)
# print(vardas)






# def sudetis_sudaugyba( skaicius1, skaicius2, skaicius3):
#     suma = skaicius1 + skaicius2
#     suma = suma * skaicius3
#     return suma

# rezultatas = sudetis_sudaugyba(5, 7, 7)                #arba jei norima pakeisti arba praleisti (5, skaicius3 = 4)
# print(rezultatas)
    






                                            ###########
# def formule(x1,x2):
    
#     suma =  x1 * x2 
#     if suma % 2 == 0:
#         return suma, "lyginis" 
#     else:
#         return suma, "nelyginis"

# x1 = float(input("pirmas skaicius: "))
# x2 = float(input("antras skaicius: "))
# daugyba = formule(x1,x2)


# print(daugyba)


                                            ##########






# def daugyba( skaicius1, skaicius2 =1, skaicius3 =1, skaicius4 =1, skaicius5 =1 ):
#     suma = skaicius1 * skaicius2 * skaicius3 * skaicius4 * skaicius5
#     return suma

# rezultatas = daugyba(2, skaicius3=4, skaicius4=2, skaicius5=3)   
# print(rezultatas)




# def vardai(vardas1="bevardis", vardas2="bevardis", vardas3="bevardis", vardas4="bevardis", vardas5="bevardis"):
#     tekstas = (f" {vardas1}  {vardas2}  {vardas3}  {vardas4}  {vardas5}")
#     return tekstas

# visi_vardai = vardai("Tomas", vardas3="Mantas", vardas4="Gytis", vardas5="Nerius")
# print(visi_vardai)





# def teksto_modifikacija(tekstas,uppercase = False):
#     if uppercase:
#         tekstas = tekstas.upper()
#     else:
#         tekstas = tekstas.lower()
#     return tekstas

# naujas_tekstas = teksto_modifikacija("Mano vardas Sarunas", True)        #True-didziosiom, False-mazosiom #
# print(naujas_tekstas)



                            #######################   ARGS  #############


# def atspauzdink_visus(*args):
#     for item in args:
#         print(f"{item}, ")

# atspauzdink_visus(1231,6545,8798,8,77,88,"tekstas", 54, 55)

########



# def atspauzdink_visus(*args):
#     for item in args:
#         print(f"{item}, ")

# def suma(*args):
#     return sum(args)
# def maximum(*args):
#     return max(args)
# atspauzdink_visus(1231,6545,8798,8,77,88, 54, 55)

# gauta_suma = suma(1231,6545,8798,8,77,88, 54, 55)
# print("----------")
# print(gauta_suma)

# gautas_max = maximum(1231,6545,8798,8,77,88, 54, 55)
# print("----------")
# print(gautas_max)










# def atspauzdink_visus_zodyno_duomenis(**kwargs):
#     for key, value in kwargs.items():
#         print(f"key:{key} - Value:{value}")

# atspauzdink_visus_zodyno_duomenis(vardas = "Rokas", profesija = "programuotojas", pomegis = "futbolas", amzius = 99 )                                                                                                  



# def funkcija(a, b, c, *args, d = 11, e = 22, **kwargs):
#     print(type(args), args)
#     print(type(kwargs), kwargs)

# funkcija(9,8,7,9999,3,4,5678888,d=777,e = 222, zodis = "medis", metu_laikas = "pavasaris", oras = "silta")


    

# def kvadratu(skaicius):
#     return skaicius ** 2



                              ######  LAMBDA KVADRATU #################################

# kvadratu_lambda = lambda skaicius : skaicius ** 2
# daugyba = lambda x, y : x * y
# sarasas = [8,4,5,6,9]
# rezultatas_kvadratu = kvadratu_lambda(3)
# rez_kvadr_saras = map(lambda skaicius : skaicius ** 2, sarasas)
# for item in rez_kvadr_saras:
#     print(item)

















