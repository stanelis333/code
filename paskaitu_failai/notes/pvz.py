
# class Temperature:
#     def __init__(self, celsius=0):
#         self.celsius = celsius
#     @property
#     def celsius(self):
#         return self._celsius
#     @property
#     def farenheit(self):
#         self._farenheit = (self.celsius * 9/5) + 32
#         return self._farenheit
    
#     @celsius.setter
#     def celsius(self, value):
#         self._celsius = value
#     @farenheit.setter
#     def farenheit(self, value):
#         self._farenheit = value


# temp = Temperature(19)
# print(f"Celsius: {temp._celsius}")  
# print(f"Farenheit: {temp.farenheit}")  


#nr.2

class User():
    def __init__(self, password):
        self._password = password

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def ar_saugus(self):
        if len(self._password) > 8:
            return "saugus slaptazodis"
        else:
            return "nesaugus slaptazodis"
passw = input('Iveskite slaptazodi: ')
user = User(passw)
print(user.password)
print(user.ar_saugus)

