from math import pi
from shape import Shape

#สี่เหลื่ยม
class Square(Shape):
    def __init__(self) -> None:
        super().__init__()
        self.shape = 'Square'
        self.__lenght = 0

    @property
    def lenght(self):
        return self.__lenght

    @lenght.setter
    def lenght(self,value):
        self.lenght = value

    def compute_area(self):
        super().compute_area()
        self.area = self.lenght ** 2

    def print_square(self):
        print(f'{self.shape} Area = {self.area:.2f}')

#วงกลม
class Circle(Shape):
    def __init__(self) -> None:
        super().__init__()
        self.shape = 'Circle'
        self.__radius = 0

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self,value):
        self.radius = value

    def compute_area(self):
        super().compute_area()
        self.area = pi * (self.radius ** 2)

    def print_circle(self):
        print(f'{self.shape} Area = {self.area:.2f}')

#สามเหลื่ยม
class Triangle(Shape):
    def __init__(self) -> None:
        super().__init__()
        self.shape = 'Triangle'
        self.__base = 0
        self.__high = 0

    @property #getter base
    def base(self):
        return self.__base

    @base.setter #seter base
    def base(self,value):
        self.base = value

    @property #getter high
    def high(self):
        return self.__high

    @high.setter #seter high
    def high(self,value):
        self.high = value

    def compute_area(self):
        super().compute_area()
        self.area = 0.5 * self.base * self.high

    def print_triangle(self):
        print(f'{self.shape} Area = {self.area:.2f}')