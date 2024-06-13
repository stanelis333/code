



class Skaitytojas:
    def __init__(self, ID):
        self.ID = ID
        self.paimtos_knygos = {}

    def __str__(self):
        return f"ID: {self.ID}, Paimtų knygų kiekis: {len(self.paimtos_knygos)}"
