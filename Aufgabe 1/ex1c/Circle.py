import math

import Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def getarea(self):
        return (self.radius**2)*math.pi
