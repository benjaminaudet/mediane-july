class CompteBancaire:
    def __init__(self, numéro, titulaire, solde, découvert_autorisé) -> None:
        self.__numéro = numéro
        self.__titulaire = titulaire
        self.__solde = solde
        self.__découvert_autorisé = découvert_autorisé

    def get_numéro(self):
        return self.__numéro

    def get_titulaire(self):
        return self.__titulaire

    def get_solde(self):
        return self.__solde

    def diminuer_solde(self, montant):
        self.__solde -= montant

    def augmenter_solde(self, montant):
        self.__solde += montant

    def get_découvertAutorisé(self):
        return self.__découvert_autorisé

    def vérification_dépassement_découvert_autorisé(self, montant) -> None:
        if self.__solde - montant < self.__découvert_autorisé:
            raise Exception("L'opération dépasse le découvert autorisé.")

    def débiter(self, montant) -> int:
        self.vérification_dépassement_découvert_autorisé(montant)
        self.diminuer_solde(montant)
        return montant

    def créditer(self, montant) -> None:
        self.augmenter_solde(montant)

    def virer(self, montant, compte_bancaire) -> None:
        self.débiter(montant)
        compte_bancaire.créditer(montant)
        print(
            f'Virement effectué avec succès depuis le compte {self.__numéro} appartenant à {self.__titulaire} vers le compte {compte_bancaire.get_numéro()} appartement à {compte_bancaire.get_titulaire()}')

    def type(self):
        return type(self).__name__

    def display(self) -> None:
        print('##############')
        print(f'numéro: {self.__numéro}')
        print(f'titulaire: {self.__titulaire}')
        print(f'solde: {self.__solde}')
        print(f'découvert_autorisé: {self.__découvert_autorisé}')
        print(f'type: {self.type()}')
        print('##############')


class CompteEpargne(CompteBancaire):
    def __init__(self, numéro, titulaire, solde, taux_interet):
        super().__init__(numéro, titulaire, solde, 0)
        self.__taux_interet = taux_interet

    def display(self) -> None:
        print('##############')
        print(f'numéro: {self.get_numéro()}')
        print(f'titulaire: {self.get_titulaire()}')
        print(f'solde: {self.get_solde()}')
        print(f'découvert_autorisé: {self.get_découvertAutorisé()}')
        print(f'type: {self.type()}')
        print(f'taux_interet: {self.__taux_interet}')
        print('##############')


compte_ben = CompteBancaire('123456789', 'Benjamin Audet', 543, 0)
compte_epargne_ben = CompteEpargne('543216789', 'Benjamin Audet', 100, 2)
compte_damien = CompteBancaire('987654321', 'Damien Verbeke', 852, 200)
compte_ben.display()

try:
    compte_ben.virer(300, compte_damien)
    compte_ben.display()
    compte_damien.display()

    compte_ben.virer(100, compte_epargne_ben)
    compte_ben.display()
    compte_epargne_ben.display()

    compte_ben.virer(300, compte_damien)
    compte_ben.display()
    compte_damien.display()
except Exception as e:
    print('Erreur:', end=" ")
    print(e)
