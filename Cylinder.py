import math


class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def diameter(self):
        return self.radius*2

        # Ruumala
    def volume(self):
        return math.pi * self.radius ** 2 * self.height

        #Põhjapindala
    def base_area(self):
        return math.pi * self.radius ** 2

        #Küljepinada
    def lateral_area (self):
        return 2 * math.pi * self.radius * self.height

        #Kogu pindala
    def total_area(self):
        return 2 * self.base_area() + self.lateral_area()

    def __str__(self):
        return (f'Diameeter: {self.diameter()}\n'
                f'Põhjapindala: {self.base_area()}\n'
                f'Küljepindala: {self.lateral_area()}\n'
                f'Kogu pindala: {self.total_area()}\n')

