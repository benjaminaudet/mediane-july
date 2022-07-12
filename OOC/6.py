class Voiture:
    nb_roues = 4

    def __init__(self, vitesse, nb_passagers):
        self.vitesse = vitesse
        self.nb_passagers = nb_passagers

    @staticmethod
    def prompt():
        print('Je suis la voiture.')


(print('nb roues'))
print(Voiture.prompt())
exit()
voiture = Voiture(50, 3)
print(voiture.vitesse, voiture.nb_roues)
