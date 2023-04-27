# Գրել MyList class, որը կունենա գրեթե բոլոր այն մեթոդները և ֆունկցիոնալությունը, որը ունի list class-ը առանց ժառանգելու:

class Mylist:
    def __init__(self, iterable_):
        self.is_iterable(iterable_)
        self.__iterable_ = list(iterable_)

    @staticmethod
    def is_iterable(iterable1):
        if not isinstance(iterable1, (list, tuple, str, set, dict)):
            raise Exception('Must be iterable object')

    @property
    def my_list(self):
        return self.__iterable_

    def __getitem__(self, item):
        return self.__iterable_[item]

    def __setitem__(self, key, value):
        self.__iterable_[key] = value

    def __delitem__(self, key):
        del self.__iterable_[key]

    def __str__(self):
        return f"{self.__iterable_}"

    def __len__(self):
        return len(self.__iterable_)

    def append(self, a):
        self.__iterable_.append(a)

    def sort(self):
        if all(isinstance(i, (int, float)) for i in self.__iterable_) or \
                all(isinstance(i, str) for i in self.__iterable_):
            return self.__iterable_.sort()
        else:
            raise Exception('all in the iterable object must be integers')

    def pop(self):
        self.__iterable_.pop()

    def clear(self):
        self.__iterable_.clear()

    def reverse(self):
        return self.__iterable_.reverse()

    def copy(self):
        return self.__iterable_.copy()

    def index(self, i):
        return self.__iterable_.index(i)

    def count(self, c):
        return self.__iterable_.count(c)

    def extend(self, iterable2):
        self.is_iterable(iterable2)
        return self.__iterable_.extend(iterable2)

    def remove(self, r):
        self.__iterable_.remove(r)


my_list = Mylist([60, 78, 5, 53, 98])
print(my_list)
print(my_list[2])
my_list[2] = 35
print(my_list)
my_list.append(90)
print(my_list)
del my_list[0]
print(my_list)
my_list.sort()
print(my_list)
print(len(my_list))
my_list.reverse()
print(my_list)
print(my_list.index(90))
