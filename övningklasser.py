import math

class GeometricShape:
    def __init__(self, width, length):
        self.width = width
        self.length = length
        self.area = 0
        self.perimeter = 0
    
    def calculate_area(self):
        pass        #self.area = self.width * self.length
    
    def calculate_perimeter(self):
        pass        #self.perimeter = 2 * (self.width + self.length)

class Rectangle(GeometricShape):
    def __init__(self, width, length):
        super().__init__()
        self.width = width
        self.length = length

    def calculate_area(self):
        self.area = self.width * self.length

    def calculate_perimeter(self):
        self.perimeter = 2 * (self.width + self.length)

class Circle(GeometricShape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    def calculate_area(self):
        self.area = math.pi * self.radius ** 2
    def calculate_perimeter(self):
        self.perimeter = math.pi * self.radius
    