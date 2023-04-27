# Գրել հետևյալ ծրագիրը․
#    - input-ի միջոցով օգտատիրոջից կհարցնի երկրաչափական պատկերի անվանումը
#      (square (քառակուսի), rectangle (ուղղանկյուն), circle (շրջան), triangle (եռանկյուն)),
#      եթե այլ անվանում է մուտքագրել, նորից հարցնի և տեղեկացնի, որ սխալ է մուտքագրվածը,
#    - սահմանել առանձին ֆունկցիաներ տարբեր երկրաչափական պատկերների մակերեսները հաշվելու համար
#      (քառակուսի, ուղղանկյուն, շրջան, եռանկյուն),
#      ֆունկցիաներից ամեն մեկը պետք է ընդունի համապատասխան քանակի արգումենտներ՝
#       -- քառակուսու համար պետք է ստանա 1 արգումենտ (քառակուսու կողմը՝ a) և վերադարձնի՝ a * a,
#       -- ուղղանկյան համար պետք է ստանա 2 արգումենտ (ուղղանկյան երկարությունը և լայնությունը՝ a, b) և վերադարձնի՝ a * b,
#       -- շրջանի համար պետք է ստանա 1 արգումենտ (շրջանի շառավիղը՝ r) և վերադարձնի՝ pi * r **2,
#       -- եռանկյան համար պետք է ստանա 2 արգումենտ (եռանկյան կողմը և բարձրությունը՝ a, h) և վերադարձնի՝ a * h / 2,
#    - սահմանել ֆունկցիա, որը կընդունի մեկ արգումենտ՝ երկրաչափական պատկերի անվանումը,
#       - ֆունկցիայի ներսում input-ի միջոցով օգտատիրոջից կհարցնի համապատասխան երկրաչափական պատկերի տվյալները,
#       - կվերադարձնի տրված պարամետրերով երկրաչափական պատկերների մակերեսը,
#    - կարող եք օգտագործել try / except / else / finally կոնստրուկցիան,
#    օրինակ՝ 1․ օգտատերը input-ի միջոցով մուտքագրեց "rectangle",
#            2․ ծրագիրը կհարցնի ուղղանկյան լայնությունը և երկարությունը մեկ input-ի միջոցով (օրինակ՝ 3, 5)
#            3․ կտպի մակերեսը՝ 15,
#            4․ նորից կվերադառնա առաջին քայլին։

import math


def square(a: list):
    if len(a) == 1:
        return a[0] ** 2
    return 'Incorrect parameters'


def rectangle(a: list):
    if len(a) == 2:
        return a[0] * a[1]
    return 'Incorrect parameters'


def circle(a: list):
    if len(a) == 1:
        return a[0] ** 2 * math.pi
    return 'Incorrect parameters'


def triangle(a: list):
    if len(a) == 2:
        return a[0] * a[1] / 2
    return 'Incorrect parameters'


geometry_dict = {'1': 'square', '2': 'rectangle', '3': 'circle', '4': 'triangle'}
geometry_message = """Enter number: 1 for square, 2 for rectangle, 3 for circle, 4 for triangle, ("exit" for end)
n = """
while True:
    num = input(geometry_message)
    if num in geometry_dict.keys():
        try:
            a = input("Input parameter(s) (separate must be space): ")
            a = [float(i) for i in a.split()]
            if all([True if i > 0 else False for i in a]):
                print(eval(geometry_dict[num] + f'({a})'))
            else:
                print('Numbers must be positive')
        except Exception as text:
            print(text)
    elif num == 'exit':
        break
    else:
        print('Incorrect choice')
