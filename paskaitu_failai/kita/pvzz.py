





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
        if self.is_strong_password(self._password):
            return "saugus slaptazodis"
        else:
            return "nesaugus slaptazodis"

    def is_strong_password(self, password):
        if len(password) < 8:
            return False
        
        has_upper = False
        has_lower = False
        has_digit = False
        
        for char in password:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isdigit():
                has_digit = True

        return has_upper and has_lower and has_digit

passw = input('Iveskite slaptazodi: ')
user = User(passw)
print(user.password)
print(user.ar_saugus)