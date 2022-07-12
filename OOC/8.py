class Animal:
    def __init__(self, name):
        self.point_de_vie = 100
        self.name = name

    def display(self):
        print(f'I am {self.name} and I have {self.point_de_vie} pv')

    def dormir(self):
        self.point_de_vie += 1
        self.display()

    def die(self):
        self.point_de_vie = 0
        self.display()


class Carnivore(Animal):
    def __init__(self, name):
        super().__init__(name)

    def chasser(self, animal):
        animal.die()
        self.point_de_vie += 5
        self.display()


class Herbivore(Animal):
    def __init__(self, name):
        super().__init__(name)

    def paturer(self):
        self.point_de_vie += 5
        self.display()


bulbizar = Herbivore('bulbizar')
dracaufeu = Carnivore('dracaufeu')
dracaufeu.display()
bulbizar.paturer()
bulbizar.paturer()
bulbizar.paturer()
bulbizar.dormir()
dracaufeu.display()
dracaufeu.chasser(bulbizar)
dracaufeu.dormir()
