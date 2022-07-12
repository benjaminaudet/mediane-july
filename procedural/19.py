somme = int(input("Entrez une somme :\n"))
print('\n')
choix = int(input('Options [ 1 : euros -> dollars, 2 : dollars -> euros ]\n'))
if choix == 1:
    print(f'{somme} dollars valent {int(somme*0.9)} euros')
elif choix == 2:
    print(f'{somme} euros valent {int(somme*1.1)} dollars')
