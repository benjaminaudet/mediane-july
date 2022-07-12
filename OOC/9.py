class Joueur():
    def __init__(self, nom, position, goals) -> None:
        self.nom = nom
        self.position = position
        self.goals = goals

    @staticmethod
    def compare(joueur_1, joueur_2):
        print(f'Comparaison de "{joueur_1.nom}" et "{joueur_2.nom}":')
        print(
            f'- Joueur 1: {joueur_1.goals} buts marqués, {joueur_1.nom}, {joueur_1.position}'
        )
        print(
            f'- Joueur 2: {joueur_2.goals} buts marqués, {joueur_2.nom}, {joueur_2.position}'
        )
        best_one = joueur_1 if joueur_1.goals > joueur_2.goals else joueur_2
        worst_one = joueur_1 if joueur_1.goals < joueur_2.goals else joueur_2
        print(f'"{best_one.nom}" est meilleur que "{worst_one.nom}".')


ronaldo = Joueur('Ronaldo', 'attaquant', 18)
messi = Joueur('Messi', 'attaquant', 21)
Joueur.compare(ronaldo, messi)
