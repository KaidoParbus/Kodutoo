import math


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def diagonal(self):
        return math.sqrt(self.width ** 2 + self.height ** 2)

    def __repr__(self):
        return (f'a: {self.width}\nb: {self.height}\ndiagonaal: {self.diagonal()}\nümbermõõt: {self.perimeter()}\n'
                f'pindala: {self.area()}')