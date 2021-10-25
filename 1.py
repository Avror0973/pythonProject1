class Parentse:
    def __init__(self, age=29, name="Mark", height=1.75):
        self.age = age
        self.name = name
        self.height = height


class Son(Parentse):
    strenght = 4

    def set_strenght(self, s):
        self.strenght = s

    def pr(self):
        print(self.strenght)

class Daughter(Parentse):
    beaty = 10

    def set_beaty(self, b):
        self.beaty = b

    def pr(self):
        print(self.beaty)

class Dog(Parentse):
    barking_per_day = 10

    def set_barks(self, bar):
        self.barking_per_day = bar

    def pr(self):
        print(self.barking_per_day)

Alex = Son(9, "John", 1.45)
Alex.strenght = 10
Alex.pr()

Katarina = Daughter(12, "Katarina", 3.25)
Katarina.beaty = 100
Katarina.pr()

Pec = Dog(2, "Pec", 0.45)
Pec.barking_per_day = 1000000000000000000000000
Pec.pr()

print("Hello update")