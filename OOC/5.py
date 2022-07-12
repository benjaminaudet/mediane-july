class Shape():
    def __init__(self, height, width):
        self.height = height
        self.width = width


class Rectangle(Shape):
    def __init__(self, height, width):
        super().__init__(height, width)

    def get_perimeter(self):
        return (self.height + self.width) * 2

    def get_surface(self):
        return self.height * self.width


if __name__ == '__main__':
    rectangle = Rectangle(5, 10)
