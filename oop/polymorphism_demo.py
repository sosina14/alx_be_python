import math
class Shape:
    def area(self):
        raise NotImplementedError("The method should be overridden in subclasses")
class Rectangle(Shape):
    def __init__(self, length , width):
        self.length = length
        self.width = width
    def area(self):
        return "Area of the rectangle is {self.length * self.width} square"
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)

