# Գրել Calculator class, որը․
#    - __init__ ում կստանա թիվ և կստուգի այդ թվի int կամ float լինելը, հակառակ դեպքում կվերադարձնի Error,
#    - կունենա միայն getter մեթոդ տրված թիվը ստանալու համար, իսկ այդ թիվը կլինի private,
#    - կունենա համապատասխան magic մեթոդներ հետևյալ գործողությունների համար (+, -, *, /, //, %, **),
#    - կունենա համապատասխան magic մեթոդներ հետևյալ գործողությունների համար (+=, -=, *=, /=, //=, %=, **=),
#    - կունենա համապատասխան magic մեթոդներ հետևյալ գործողությունների համար (==, >, >=, <, <=, !=),
#    - վերոնշյալ մեթոդները ռեալիզացված կլինեն այնպես, որ աշխատեն նաև Calculator կլասի երկու օբյեկտների համար,
#    - կունենա համապատասխան magic մեթոդներ, որոնք թույլ կտան օբյեկտը տպելուց․ ստանալ թիվը (__str__), ստանալ թիվը և
#    թվի տիպը (__repr__)։

class Calculator:
    def __init__(self, number):
        if not isinstance(number, (int, float)) and number > 0:
            raise Exception('Must be positive integer or float')
        self.__number = number

    @staticmethod
    def is_valid(n):
        if not isinstance(n, (int, float, Calculator)) and n > 0:
            raise Exception('Must be positive integer or float or Calculator')

    @property
    def number(self):
        return self.__number

    def __repr__(self):
        return f'{self.__number}, {type(self.__number)}'

    def __str__(self):
        return f"{self.__number}"

    def __add__(self, other):
        self.is_valid(other)
        if isinstance(other, Calculator):
            other = other.__number
        return Calculator(self.__number + other)

    def __radd__(self, other):
        self.is_valid(other)
        return self + other

    def __iadd__(self, other):
        self.is_valid(other)
        if isinstance(other, Calculator):
            other = other.__number
        self.__number += other
        return self

    def __sub__(self, other):
        self.is_valid(other)
        if isinstance(other, Calculator):
            other = other.__number
        return Calculator(self.__number - other)

    def __rsub__(self, other):
        self.is_valid(other)
        if isinstance(other, Calculator):
            other = other.__number
        return Calculator(other - self.__number)

    def __isub__(self, other):
        self.is_valid(other)
        if isinstance(other, Calculator):
            other = other.__number
        self.__number -= other
        return self

    def __mul__(self, other):
        self.is_valid(other)
        if isinstance(other, Calculator):
            other = other.__number
        return Calculator(self.__number * other)

    def __truediv__(self, other):
        self.is_valid(other)
        if isinstance(other, Calculator):
            other = other.__number
        return Calculator(self.__number / other)

    def __floordiv__(self, other):
        self.is_valid(other)
        if isinstance(other, Calculator):
            other = other.__number
        return Calculator(self.__number // other)

    def __mod__(self, other):
        self.is_valid(other)
        if isinstance(other, Calculator):
            other = other.__number
        return Calculator(self.__number % other)

    def __pow__(self, other):
        self.is_valid(other)
        if isinstance(other, Calculator):
            other = other.__number
        return Calculator(self.__number ** other)

    def __imul__(self, other):
        self.is_valid(other)
        if isinstance(other, Calculator):
            other = other.__number
        self.__number *= other
        return self

    def __itruediv__(self, other):
        self.is_valid(other)
        if isinstance(other, Calculator):
            other = other.__number
        self.__number /= other
        return self

    def __ifloordiv__(self, other):
        self.is_valid(other)
        if isinstance(other, Calculator):
            other = other.__number
        self.__number //= other
        return self

    def __imod__(self, other):
        self.is_valid(other)
        if isinstance(other, Calculator):
            other = other.__number
        self.__number %= other
        return self

    def __ipow__(self, other):
        self.is_valid(other)
        if isinstance(other, Calculator):
            other = other.__number
        self.__number **= other
        return self

    def __rmul__(self, other):
        self.is_valid(other)
        return self * other

    def __rtruediv__(self, other):
        self.is_valid(other)
        if isinstance(other, Calculator):
            other = other.__number
        return Calculator(other / self.__number)

    def __rfloordiv__(self, other):
        self.is_valid(other)
        if isinstance(other, Calculator):
            other = other.__number
        return Calculator(other // self.__number)

    def __rmod__(self, other):
        self.is_valid(other)
        if isinstance(other, Calculator):
            other = other.__number
        return Calculator(other % self.__number)

    def __rpow__(self, other):
        self.is_valid(other)
        if isinstance(other, Calculator):
            other = other.__number
        return Calculator(other ** self.__number)

    def __eq__(self, other):
        self.is_valid(other)
        if isinstance(other, Calculator):
            other = other.__number
        return self.__number == other

    def __gt__(self, other):
        self.is_valid(other)
        if isinstance(other, Calculator):
            other = other.__number
        return self.__number > other

    def __ge__(self, other):
        self.is_valid(other)
        if isinstance(other, Calculator):
            other = other.__number
        return self.__number >= other


my_calculator1 = Calculator(5)
my_calculator2 = Calculator(200)
print(my_calculator1)
print(my_calculator2)
print(repr(my_calculator1))
print(str(my_calculator2))
print(my_calculator1 + 500)
print(500 + my_calculator2)
print(my_calculator1 + my_calculator2)
my_calculator2 += my_calculator1
print(my_calculator2)
print(500 - my_calculator2)
print(my_calculator2 - 500)
print(my_calculator1 // 3)
print(my_calculator2 / 5)
print(5 / my_calculator2)
print(3 // my_calculator1)
print(my_calculator1 ** 2)
print(2 ** my_calculator1)
my_calculator_1 = 10 - my_calculator2
print(my_calculator1 + my_calculator2)
