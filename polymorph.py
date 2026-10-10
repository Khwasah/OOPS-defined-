'''Polymorphism: A list of Shape objects(Circle, Rectangle
, Triangle) and loop calling area().'''


class shape:
    def __init__(self,circle,rectangle,triangle):
        self.circle = circle
        self.rectangle = rectangle
        self.triangle = triangle
    def area(self):
        return self.circle, self.rectangle, self.triangle

Area = shape(3.14*5*5, 4*6, 0.5*4*7)
print("Area of Circle, Rectangle and Triangle is: ", Area.area())

# OR


import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# List of Shape objects
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 8)
]

# Polymorphic behavior
for shape in shapes:
    print(f"Area = {shape.area():.2f}")