import math


# Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calc_perimeter(self):
        print(2 * math.pi * self.radius)

    def calc_area(self):
        print(math.pi * self.radius * self.radius)


circle1 = Circle(3)
circle1.calc_area()
circle1.calc_perimeter()
