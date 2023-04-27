from math import log2


# 1․ Գրել երեք դեկորատոր, որոնք կիրառելով որոշակի ֆունկցիայի վրա, կփոխենք այդ ֆունկցիայի
# output - ի գույնը  կանաչի, կարմիրի, կապույտի։
# Python - ի output - ի գույնը փոխելու համար string - ի սկզբում գործածում ենք \033 այս հաջորդականությունը
# և գույնի կոդը։ Օրինակ ` որպեսզի տեքստը տպվի կանաչ, կարող ենք
# օգտագործել '\033[92m', այսինքն՝
# print('\033[92mThis text will be in green\033[0m')
# \033[0m - վերացնել բոլոր փոփոխությունները
# Գույն	      Տեքստ (մուգ, բաց)	     Ֆոն (մուգ, բաց)
# Սև	            30 կամ 90              40 կամ 100
# Կարմիր	      31 կամ 91	           41 կամ 101
# Կանաչ	      32 կամ 92	           42 կամ 102
# Դեղին	      33 կամ 93	           43 կամ 103
# Կապույտ	      34 կամ 94	           44 կամ 104
# Մանուշակագույն	35 կամ 95	           45 կամ 105
# Փիրուզագյուն	36 կամ 96	           46 կամ 106
# Սպիտակ	      37 կամ 97	           47 կամ 107
# Արժեքի կոդ
# 0	    Սկզբնական արժեքի վերադարձ
# 1	    Հաստ
# 3	    Շեղ
# 4	    Ընդգծված
# 7	    Ֆոնի և տեքստի գույների տեղերի փոփոխություն
# 9       Ջնջված

def print_green(func):
    def inner(text):
        print(f'\033[92m{text}\033[0m')

    return inner


def print_red(func):
    def inner(text):
        print(f'\033[91m{text}\033[0m')

    return inner


def print_blue(func):
    def inner(text):
        print(f'\033[94m{text}\033[0m')

    return inner


@print_green
def print_color1(text):
    return text


@print_blue
def print_color2(text):
    return text


@print_red
def print_color3(text):
    return text


print_color1('text color changed')
print_color2('text color changed')
print_color3('text color changed')


# 2․ Գրել դեկորատոր, որը.
# - կվերցնի հետևյալ ֆունկցիայի բոլոր արգումենտների երկու հիմքով լոգարիթմները,
# - կկատարի համապատասխան գործողությունը ֆունկցիայի մեջ,
# - կվերադարձնի ստացվածի վրա նույնպես լոգարիթմ կիրառած պատասխանը,
# ֆունկցիան՝
# def f(a, b):
#     return a - b
# օրինակ՝ f(1024, 64) -> 2:

def log_2(func):
    def inner(a, b):
        return log2(func(log2(a), log2(b)))

    return inner


@log_2
def f(a, b):
    return a - b


print(f(1024, 64))


# 3․  Գրել դեկորատոր, որը․
# - cache կանի ֆունկցիայի կանչի արդյունքները,
# - ստուգեք այն ռեկուրսիվ ֆիբոնաչիի հաջորդականության ֆունկցիայի վրա
# (պետք է աշխատի նույն կերպ, ինչպես functools - ի lru_cash դեկորատորը)։

def fib_without_cache(func):
    cache = {}

    def inner(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = func(*args)
            return cache[args]

    return inner


@fib_without_cache
def fib(num):
    if num < 2:
        return num
    return fib(num - 1) + fib(num - 2)


print(fib(400))
