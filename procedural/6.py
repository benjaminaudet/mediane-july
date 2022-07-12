car_brands = ['Volvo', 'BMW', 'Toyota']


def print_car_brands():
    for i, brand in enumerate(car_brands):
        if i == 0:
            print('I like', end=" ")
        if i + 1 == len(car_brands):
            print('and {}'.format(brand), end=".")
            break
        print(brand, end=", ")


print_car_brands()
