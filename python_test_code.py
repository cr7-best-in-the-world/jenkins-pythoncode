from math import pi


class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)


shapes = [Rectangle(4, 5), Circle(3), Rectangle(6, 7), Circle(4),Rectangle(2, 3), Circle(4) ]

for shape in shapes:
    print(f"area of the shape is: {shape.area()}")
