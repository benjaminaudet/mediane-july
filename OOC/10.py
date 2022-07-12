from lib2to3.pytree import Base
from multiprocessing.sharedctypes import Value


class CompteBancaire:
    def __init__(self, numéro, titulaire, solde, découvert_autorisé) -> None:
        self.__numéro = numéro
        self.__titulaire = titulaire
        self.__solde = solde
        self.__découvert_autorisé = découvert_autorisé

    def getNuméro(self):
        return self.__numéro

    def getTitulaire(self):
        return self.__titulaire

    def getSolde(self):
        return self.__solde

    def getDécouvertAutorisé(self):
        return self.__découvert_autorisé

    def vérification_dépassement_découvert_autorisé(self, montant) -> None:
        if self.solde - montant < self.découvert_autorisé:
            raise BaseException().__str__

    def débiter(self, montant) -> int:
        self.vérification_dépassement_découvert_autorisé(montant)
        self.solde -= montant
        return montant

    def créditer(self, montant) -> None:
        self.solde += montant

    def virer(self, montant, compte_bancaire) -> None:
        self.débiter(montant)
        compte_bancaire.créditer(montant)
        print(
            f'Virement effectué avec succès depuis le compte {self.numéro} appartenant à {self.titulaire} vers le compte {compte_bancaire.numéro} appartement à {compte_bancaire.titulaire}')

    def display(self) -> None:
        print('##############')
        print(f'numéro: {self.numéro}')
        print(f'titulaire: {self.titulaire}')
        print(f'solde: {self.solde}')
        print(f'découvert_autorisé: {self.découvert_autorisé}')
        print('##############')


compte_ben = CompteBancaire('123456789', 'Benjamin Audet', 543, 0)
compte_damien = CompteBancaire('987654321', 'Damien Verbeke', 852, 200)
compte_ben.display()

try:
    compte_ben.virer(300, compte_damien)
    compte_ben.display()
    compte_damien.display()
    compte_ben.virer(300, compte_damien)
    compte_ben.display()
    compte_damien.display()
except Exception as e:
    print('Erreur:', end=" ")
    print(e)
