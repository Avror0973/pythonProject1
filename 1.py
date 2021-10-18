class Main:
    pass

class Employee:
    def forma_shulera(self):
        print("Крминальный опыт - ", end='')

    def forma_vora(self):
        print("Украл - ", end='')

    def forma_asasina(self):
        print("Килы - ", end='')


class Shuler(Employee):
    def __init__(self, criminal_experience):
        self.criminal_experience = criminal_experience

    def info(self):
        super().forma_shulera()
        print(self.criminal_experience)

class Vor(Employee):
    def __init__(self, ukral):
        self.ukral = ukral

    def info(self):
        super().forma_vora()
        print(self.ukral)

class Assassin(Employee):
    def __init__(self, kills):
        self.kills = kills

    def info(self):
        super().forma_asasina()
        print(self.kills)

#Djigit Alecksand Volkonovski
Djigit = Shuler(3)
Djigit.info()

Aleksandr = Vor(3000)
Aleksandr.info()

Jeck = Assassin(27)
Jeck.info()