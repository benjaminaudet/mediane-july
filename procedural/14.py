nom = input('Entrez votre nom:')
prenom = input('Entrez votre prénom:')
age = input('Entrez votre age:')
if int(age) < 18:
    print("Vous n'êtes pas autorisé")
    exit(0)
print(f"Bienvenue {nom} {prenom}")
