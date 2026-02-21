import math


# Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calc_perimeter(self):
        print(2 * math.pi * self.radius)

    def calc_area(self):
        print(math.pi * self.radius * self.radius)


# circle1 = Circle(3)
# circle1.calc_area()
# circle1.calc_perimeter()

# Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.
# import
from datetime import date
class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob
    
    def find_age(self):
        curr_year = date.today().year
        return int(curr_year) - int(self.dob)
        
p1 = Person("aayan Ahmed", "Pakistan", "2006")
p1_age = p1.find_age()
print(p1_age)
