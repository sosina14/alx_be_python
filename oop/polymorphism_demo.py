import math

class Shape:
    def __init__(self, length , width):
        self.length = length
        self.width = width
    def area(self):
        raise NotImplementedError("error")
class Rectangle(Shape):
    def __init__(self, length , width):
        print(f"Area of the rectangle is {length * width} square")
class Circle(Shape):
    def __init__(self, radis):
        print(f"Area of the circule is {math.pi*radis*radis}")
