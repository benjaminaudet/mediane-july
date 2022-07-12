class Wheel:
    def __init__(self, radius, width):
        self.radius = radius
        self.width = width


class Car:
    def __init__(self, color, power, velocity, wheels_amount=4):
        self.wheels = [Wheel(4, 5) for x in range(wheels_amount)]
        self.color = color
        self.power = power
        self.velocity = velocity

    def speed_up(self):
        self.velocity += 5

    def speed_down(self):
        self.velocity -= 5

    def prompt(self):
        print(
            f"####\ncar\n####\nwheels: {len(self.wheels)}\npower: {self.power}\nvelocity: {self.velocity}\ncolor: {self.color}"
        )


if __name__ == "__main__":
    car_red = Car('red', 5, 0)
    car_red.speed_up()
    car_red.prompt()
    car_red.speed_down()
    car_red.prompt()
    car_blue = Car('blue', 5, 0, 3)
    car_blue.speed_up()
    car_blue.prompt()
    car_blue.speed_down()
    car_blue.prompt()
