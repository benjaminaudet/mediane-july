class Personne:
    def __init__(self, nom):
        self.nom = nom

    def display(self):
        print(self.nom)


class Etudiant(Personne):
    def __init__(self, nom, ine):
        # Personne.__init__(self, nom)
        super().__init__(nom)
        self.ine = ine

    def display(self):
        print(self.nom, self.ine)


class Professeur(Personne):
    def __init__(self, nom, spécialité):
        super().__init__(nom)
        self.spécialité = spécialité

    def display(self):
        print(self.nom, f'spé: {self.spécialité}')


personne = Personne('Jacques')
personne.display()
etudiant = Etudiant('Kevin', 5591)
etudiant.display()
prof = Professeur('Kevin', 'Mathématiques')
prof.display()
