
def is_multiple_of_15(a):
    if (a % 3 == 0 and a % 5 == 0):
        print(f'{a} est un multiple de 3 et 5')
        return
    print(f"{a} n'est un multiple de 3 et 5")


is_multiple_of_15(15)
is_multiple_of_15(9)
