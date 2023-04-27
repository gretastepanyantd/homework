#  Գրել Triangle class, որը․
#    - __init__() -ում կընդունի եռանկյան կողմերը և կստուգի արդյոք նման կողմերով եռանկյուն գոյություն ունի թե ոչ,
#      եթե կողմերը սխալ են տրված կվերադարձնի Error համապատասխան տեքստով,
#    - կունենա մեթոդ, որը կվերադարձնի եռանկյան կողմերը,
#    - կունենա մեթոդ, որը կվերադարձնի եռանկյան պարագիծը,
#    - կունենա մեթոդ, որը կվերադարձնի եռանկյան մակերեսը,
#    - կունենա մեթոդ, որը կվերադարձնի արդյոք եռանկյունը հավասարակողմ է, հավասարասրուն, թե անկանոն (կողմերը իրար = չեն)։

class Triangle:
    def __init__(self, side1, side2, side3):
        if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
            self.side1 = side1
            self.side2 = side2
            self.side3 = side3
        else:
            raise Exception('Triangle does not exist.')

    def sides(self):

        return self.side1, self.side2, self.side3

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def area(self):
        p = self.perimeter() / 2
        return (p * (p - self.side1) * (p - self.side2) * (p - self.side3)) ** 0.5

    def species(self):
        if self.side1 == self.side2 == self.side3:
            return 'Equilateral Triangle'
        elif self.side1 == self.side2 or self.side2 == self.side3 or self.side3 == self.side1:
            return 'Isosceles Triangle'
        else:
            return 'Scalene Triangle'


my_triangle = Triangle(7, 5, 10)
print(my_triangle.sides())
print(my_triangle.perimeter())
print(my_triangle.area())
print(my_triangle.species())
