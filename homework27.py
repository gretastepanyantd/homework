# Գրել BankUser class, որը․
#   - __init__() -ում կընդունի մարդու անունը, ազգանունը, տարիքը, հաշվեհամարը, գումարը հաշվեհամարի վրա, գաղտնաբառը,
#   - մինչ ինիցիալիզացնելը, կստուգի, որ ընդունված արգումենտները ճիշտ են մուտքագրված՝
#     -- անունը և ազգանունը - տառերից բաղկացած,
#     -- տարիքը - ամբողջ թիվ,
#     -- հաշվեհամարը - 16 թվանշանից բաղկացած (xxxx xxxx xxxx xxxx կամ xxxxxxxxxxxxxxxx ֆորմատով),
#     -- գումարը - դրական թիվ,
#     -- գաղտնաբառը - ամենաքիչը 8 սիմվոլից բաղկացած տեքստ,
#   - անունը, ազգանունը և տարիքը կլինեն այնպիսի ատրիբուտներ, որոնց ուղիղ հասանելիությունը կլինի պաշտպանված,
#   - հաշվեհամարը, գումարը և գաղտնաբառը կլինեն այնպիսի ատրիբուտներ, որոնց ուղիղ հասանելիությունը կլինի արգելված,
#   - կունենա մեթոդ, որը կվերադարձնի մարդու անունը և ազգանունը,
#   - կունենա մեթոդ, որը կվերադարձնի մարդու տարիքը,
#   - կունենա մեթոդ, որը կվերադարձնի հաշվեհամարը և գումարը, բայց միայն ճիշտ գաղտնաբառ հավաքելուց հետո,
#   - կունենա մեթոդ, որը կավելացնի գումար հաշվին,
#   - կունենա մեթոդ, որը կհանի գումար հաշվից, հաշվի առեք, որ գումարը բացասական չի կարող լինել։

class BankUser:
    LEN_PASSWORD = 8
    AGE = 18

    def __init__(self, name, surname, age, card, balance, password):
        if self._is_valid_name(name) and self._is_valid_name(surname) and self._is_valid_age(age) and \
                self._is_valid_card(card) and self._is_valid_balance(balance) and self._is_valid_password(password):
            self._name = name
            self._surname = surname
            self._age = age
            self.__card = card
            self.__balance = balance
            self.__password = hash(password)
        else:
            raise Exception("invalid argument")

    @staticmethod
    def _is_valid_name(n):
        return isinstance(n, str) and n.isalpha()

    @classmethod
    def _is_valid_age(cls, a):
        return isinstance(a, int) and a >= cls.AGE

    @staticmethod
    def _is_valid_card(c):
        if isinstance(c, str) and c.replace(" ", "").isdecimal():
            if len(c) == 19:
                return (c[4] + c[9] + c[14]).isspace()
            return len(c) == 16

    @staticmethod
    def _is_valid_balance(b):
        return isinstance(b, (int, float)) and b > 0

    @classmethod
    def _is_valid_password(cls, p1):
        return isinstance(p1, str) and len(p1) >= cls.LEN_PASSWORD

    def name_surname(self):
        return self._name, self._surname

    def age(self):
        return self._age

    def cart_balance(self):
        inp = input('Enter your password: ')
        if self.__password == hash(inp):
            return self.__card, self.__balance
        else:
            return 'Wrong password'

    def add_balance(self, add: [int, float]):
        if self._is_valid_balance(add):
            inp = input('Enter your password: ')
            if self.__password == hash(inp):
                self.__balance += add
                print(f"Added money: {add}. Balance: {self.__balance}")
            else:
                print('Wrong password')
        else:
            raise Exception("Money must be numeric and positive.")

    def reduce_balance(self, reduce: [int, float]):
        if self._is_valid_balance(reduce):
            inp = input('Enter your password: ')
            if self.__password == hash(inp):
                self.__balance -= reduce
                print(f"Reduced money: {reduce}. Balance: {self.__balance}")
            else:

                print('Wrong password')
        else:
            raise Exception("Money must be numeric and positive.")


my_bankUser = BankUser('Greta', 'Stepanyan', 24, '1234 1234 1234 1234', 1000, '12345678')
print(my_bankUser.name_surname())
print(my_bankUser.age())
print(my_bankUser.cart_balance())
my_bankUser.add_balance(100)
my_bankUser.reduce_balance(500)
