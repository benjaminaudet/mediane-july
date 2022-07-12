while True:
    prix_ht_str = input("Prix HT ?\n")
    if prix_ht_str == '0' or prix_ht_str == '':
        print("Au revoir!")
        exit(0)
    prix_ht_int = int(prix_ht_str)
    print(f"Prix TTC : {int(prix_ht_int * 1.2)}")
