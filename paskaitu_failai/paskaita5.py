# def pasisveikinti(vardas):
#     print(f"Sveikas, {vardas}")

# pasisveikinti("Tomas")
# pasisveikinti("Jonas")
# pasisveikinti("")

# Sveikas, Tomas
# Sveikas, Jonas
# Sveikas,

# def kvadratas(skaicius):
#     kvadratu = skaicius ** 2
#     print(kvadratu)

# kvadratas(2)
# 4



                                            ############
# class kate:
#     def __init__(self, spalva, kojos):
#         self.spalva = spalva
#         self.kojos = kojos

#     def __str__(self):
#         return f" spalva: {self.spalva}\n kojos: {self.kojos}"

# kate1 = kate("Ruda", 4)
# print(kate1)



# class sportas:
#     def __init__(self, lauko, vidinis ):
#         self.lauko = lauko
#         self.vidinis = vidinis

#     def __str__(self):
#         return f"Lauko: {self.lauko}\nVidinis: {self.vidinis}"
    
# sportas1 = sportas("futbolas", "Stalo tenisas")
# print(sportas1)




                                    ###########


# class MyClass:
#     def __init__(self):
#         self.public = "public"
#         self._protected = "protected"
#         self.__private = "private"

#     def kazkas(self):
#         print("hey")

# obj = MyClass()
# print(obj.public)
# print(obj._protected)
# print(obj._MyClass__private)

# obj.kazkas()

                                            ##############

# class Person:
#     def __init__(self, vardas, metus, asmens_kodas="nenurodyta"):
#         self.vardas = vardas
#         self.metus = metus
#         self.asmens_kodas = asmens_kodas

#     def vardas_didziosiomis(self):
#         return self.vardas.upper()

#     def __str__(self):
#         return f"vardas: {self.vardas} | metai: {self.metus} | asmens_kodas: {self.asmens_kodas}"

#     # def __str__(self):
#     #     return f"spalva: {self.spalva}, kojos:{self.kojos}"

# zmogus1 = Person("Rokas", 1988)
# zmogus2 = Person("Jonas", 1956, 45645645)
# zmogus3 = Person("John", 1999,  44456456)

# # print(zmogus1)
# # print(zmogus2)
# # print(zmogus3)
# # print(zmogus3.vardas_didziosiomis())
# # print(zmogus1.metus)



                   #######################################


"""
class sakinys:
    def __init__(self, oro_salygos, krituliai):
        self.oro_salygos = oro_salygos
        self.krituliai = krituliai  

    def __str__(self):
        return f"{self.oro_salygos}, {self.krituliai}"
    def atbulai(self):
        return f"{self.oro_salygos[::-1]} {self.krituliai[::-1]} "
    def tekstas_mazosiomis(self):
        return f"{self.oro_salygos.casefold()}"
    def tesktas_didziosiomis(self):
        return f"{self.oro_salygos.upper()}"
    
    def kiek_ko (self):
        zodziu_skaicius = len(self.krituliai.split())
        didziosios = 0
        mazosios = 0
        skaiciai = 0
        for char in self.krituliai:
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

vakar = sakinys("DeBeSuoTaS OrAs", "lengvas lietus")
siandien = sakinys("Sauletas oras", "nera lietaus")
rytoj = sakinys("Labai debesuota", "LABAI stiprus lietus999")

print(siandien)
print(vakar.atbulai())
print(vakar.tekstas_mazosiomis())
print(vakar.tesktas_didziosiomis())
print(rytoj.kiek_ko())                   

"""