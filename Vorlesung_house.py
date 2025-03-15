import math as m


class Building:
    def __init__(self, year, address):
        self.year = year
        self.address = address
    def age(self):
        return 2025 - self.year



class House(Building):
    def __init__(self, year, address, corner, width, height):
        super().__init__(year, address)    #ruft den Konstruktor der Oberklasse auf
        self.corner = corner
        self.width = width
        self.height = height

    def area(self):
        return self.width ** 2

class Tower(Building):
    def __init__(self, year, address, radius, height):
        super().__init__(year, address)
        self.radius = radius
        self.height = height
    def area(self):
        return m.pi * self.radius ** 2

class Castle(House):
    def __init__(self, year, address, corner, width, height, tower_radius):
        super().__init__(year, address, corner, width, height)
        self.tower_radius = tower_radius
    def area(self):
        return super().area() + 4 * m.pi * self.tower_radius ** 2