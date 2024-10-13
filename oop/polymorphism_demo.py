import math
class Shape:
    def area(self):
        raise NotImplementedError("error")
class Rectangle(Shape):
    def __init__(self, length , width):
        self.length = length
        self.width = width
        print(f"Area of the rectangle is {length * width} square")
class Circle(Shape):
    def __init__(self, radius):
        self.radius = rasius
        print(f"Area of the circule is {math.pi*radis*radis}")
