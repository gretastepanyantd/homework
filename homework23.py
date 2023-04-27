import math
from datetime import datetime


# 1․ Գրել ֆունկցիա, որը․
#    - որպես արգումենտ կընդունի շրջանագծի շառավիղը (r) և սեկտորի անկյունը (alpha) ռադիաններով արտահայտված,
#    - կհաշվի և կտպի համապատասխան շառավղով և անկյունով շրջանի մակերեսը,
#    - բանաձևը՝ S = (pi * r ** 2) * alpha / 360, բանաձևի մեջ alpha-ն արտահայտված է աստիճաններով։

def circle_area(r, alpha):
    degree = math.degrees(alpha)
    s = (math.pi * r ** 2) * degree / 360
    return s


print(circle_area(5, 60))


# 2․ Գրել ծրագիր, որը․
#    - կստանա 3 արգումենտ՝ տարի, ամիս, օր,
#    - կտպի թե նշված օրն շաբաթվա որ օրն է։


def date(yy, mm, dd):
    d = "MTWTFSS"
    a = datetime(yy, mm, dd)
    return d[a.weekday()]


print(date(2023, 4, 3))


# 3․ Գրել ֆունկցիա, որը․
#    - կստանա արգումենտ արաբական բնական թիվ (0-ից մեծ),
#    - կվերադրձնի այդ թիվը հռոմեական տեսքով,
#    հռոմեական թվերի համարժեքները՝ I-1, V-5, X-10, L-50, C-100, D-500, M-1000,
#    օրինակ՝ 15 -> XV,
#            72 -> LXXII,
#            9 -> IX:

def roman_number(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
           100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
           "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
    while number:
        div = number // num[i]
        number %= num[i]
        while div:
            print(sym[i], end="")
            div -= 1
        i -= 1


roman_number(72)
