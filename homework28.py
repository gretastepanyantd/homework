from abc import ABC, abstractmethod
from math import pi, cos, radians


# 1․ Գրել Shape abstract class, որը․
#    - կունենա __init__(), perimetr(), area() աբստրակտ մեթոդներ։
# 2․ Գրել Circle class, որը կժառանգի Shape class-ից, որը․
#    - __init__() -ում կընդունի շրջանագծի շառավիղը,
#    - մինչ ինիցիալիզացնելը, կստուգի, որ ընդունված արգումենտը ճիշտ մուտքագրված լինի (պետք է լինի դրական թիվ),
#    - կվերախմբագրի Shape class-ի perimetr() և area() մեթոդները շրջանագծի համար։
# 3․ Գրել Rectangle class, որը կժառանգի Shape class-ից, որը․
#    - __init__() -ում կընդունի ուղղանկյան լայնությունը և երկարությունը,
#    - մինչ ինիցիալիզացնելը, կստուգի, որ ընդունված արգումենտները ճիշտ մուտքագրված լինեն (պետք է լինեն դրական թվեր),
#    - կվերախմբագրի Shape class-ի perimetr() և area() մեթոդները ուղղանկյան համար։
# 4․ Գրել Triangle class, որը կժառանգի Shape class-ից, որը․
#    - __init__() -ում կընդունի
#      -- կամ եռանկյան երեք կողմերը,
#      -- կամ մեկ կողմը և բարձրությունը,
#      -- կամ երկու կողմերը և այդ կողմերի կազմած անկյունը,
#    - մինչ ինիցիալիզացնելը, կստուգի, որ ընդունված արգումենտները ճիշտ մուտքագրված լինեն,
#    - կվերախմբագրի Shape class-ի perimetr() մեթոդը եռանկյան համար,
#    - եռանկյան մակերեսը կհաշվի 3 տարբերակով, կախված մուտքագրված պարամետրերից․
#      1) S = (p * (p - a) * (p - b) * (p - c)) ^ 0.5   , որտեղ a, b, c - եռանկյան կողմերն են, p - եռանկյան կիսապարագիծը,
#      2) S = a * h / 2                                 , որտեղ a - եռանկյան կողմը, h = եռանկյան բարձրությունը,
#      3) S = a * b * sin(alpha) / 2 ,
# որտեղ a, b - եռանկյան կողմերն են, alpha - եռանկյան a և b կողմերի կազմած անկյունը։


class ShapeAbstract(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def perimetr(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Circle(ShapeAbstract):
    def __init__(self, r):
        if self.isvalid_radius(r):
            self.__r = r
        else:
            raise Exception('invalid argument')

    @staticmethod
    def isvalid_radius(radius):
        return isinstance(radius, (int, float)) and radius > 0

    def perimetr(self):
        return 2 * pi * self.__r

    def area(self):
        return pi * self.__r ** 2


class Rectangle(ShapeAbstract):
    def __init__(self, width, length):
        if self.isvalid_param(width) and self.isvalid_param(length):
            self.__width = width
            self.__length = length
        else:
            raise Exception('invalid argument')

    @staticmethod
    def isvalid_param(width):
        return isinstance(width, (int, float)) and width > 0

    def perimetr(self):
        return (self.__width + self.__length) * 2

    def area(self):
        return self.__width * self.__length


class Triangle(ShapeAbstract):
    def __init__(self, a=None, b=None, c=None, h=None, angle=None):
        if a and self.is_valid_side(a):
            self.a = a
        else:
            self.a = None
        if b and self.is_valid_side(b):
            self.b = b
        else:
            self.b = None
        if c and self.is_valid_side(c):
            self.c = c
        else:
            self.c = None
        if h and self.is_valid_side(h):
            self.h = h
        else:
            self.h = None
        if angle and self.is_valid_angle(angle):
            self.angle = angle
        else:
            self.angle = None

        if a and b and c:
            if not self.is_valid_triangle(self.a, self.b, self.c):
                raise Exception('The triangle is not exists')
        elif a and b and angle:
            self.c = self.calc_c(self.a, self.b, self.angle)
            if not self.is_valid_triangle(self.a, self.b, self.c):
                raise Exception('The triangle is not exists')

    @staticmethod
    def calc_c(a, b, angle):
        return (a ** 2 + b ** 2 - 2 * a * b * cos(radians(angle))) ** 0.5

    @staticmethod
    def is_valid_triangle(a, b, c):
        return a + b > c and a + c > b and b + c > a

    @staticmethod
    def is_valid_side(a):
        return isinstance(a, (int, float)) and a > 0

    @staticmethod
    def is_valid_angle(a):
        return isinstance(a, (int, float)) and 0 < a < 180

    def perimetr(self):
        if self.a and self.b and self.c:
            return self.a + self.b + self.c
        else:
            return 'Unknown'

    def area(self):
        if self.a and self.b and self.c:
            p = self.perimetr() / 2
            return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
        elif self.a and self.h or self.b and self.h or self.c and self.h:
            return self.a * self.h / 2
        else:
            return 'Unknown'


my_Circle = Circle(5.0)
print(my_Circle.perimetr())
print(my_Circle.area())

my_Rectangle = Rectangle(8, 10.5)
print(my_Rectangle.perimetr())
print(my_Rectangle.area())

my_Triangle = Triangle(a=3, b=4, c=5)
print(my_Triangle.perimetr())
print(my_Triangle.area())

my_Triangle2 = Triangle(a=5, h=8)
print(my_Triangle2.perimetr())
print(my_Triangle2.area())

my_Triangle3 = Triangle(a=3, b=4, angle=45)
print(my_Triangle3.area())
print(my_Triangle3.perimetr())
