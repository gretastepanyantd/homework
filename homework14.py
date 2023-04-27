import time
import random

# 1․ Գրել ծրագիր, որը․
#    - կունենա անուններից կազմված list,
#    - հերթով կտպի այն անունները, որոնց երկարությունը 5-ից մեծ չէ,
#    - ամեն անունը տպելուց հետո հաջորդ անունը կտպի 3 վայրկյան հետո։

name_list = ['Ani', 'Gohar', 'Hasmik', 'Vardan', 'Karen', 'Gurgen']
for i in name_list:
    if len(i) <= 5:
        time.sleep(3)
        print(i)


# 2. Գրել ֆունկցիա, որը․
#    - կունենա մեկ արգումենտ, որը կլինի ամբողջ թիվ (կարող է լինել և՛ դրական, և՛ բացասական),
#    - եթե թվի թվանշանների քանակը զույգ է, կստուգի արդյոք թվի առաջին կեսի թվանշանների գումարը հավասար է երկրորդ
#      կեսի թվանշանների գումարին, թե ոչ,
#    - եթե թվի թվանշանների քանակը կենտ է, կստուգի նախորդ պայմանի ճշտությունը, ապա կստուգի նաև մեջտեղի թվանշանի
#      զույգ և կենտ լինելը,
#      եթե զույգ է, կտպի True, եթե կենտ՝ False,
#    օրինակ՝ 1238 -> False, քանի որ 1+2 != 3+8
#            1845 -> True, քանի որ 1+8 = 4+5
#            18545 -> False, քանի որ 1+8 = 4+5 և 5-կենտ է,
#            48257 -> True, քանի որ 4+8 = 5+7 և 2-զույգ է։


def even_odd(n):
    if n != 0 and type(n) == int:
        n = str(n)
        if len(n) % 2 == 0:
            return sum({int(i) for i in n[:len(n) // 2]}) == sum({int(i) for i in n[len(n) // 2:]})
        else:
            return sum({int(i) for i in n[:len(n) // 2]}) == sum({int(i) for i in n[len(n) // 2 + 1:]}) \
                and int(n[len(n) // 2]) % 2 == 0
    else:
        return 'Invalid value entered\n must enter an integer other than 0'


print(even_odd(48257))

# 3․ Գրել պարային զույգեր կազմելու ծրագիր, որը․
#    - կունենա երկու անունների list, list-երի երկարությունները կարող են տարբեր լինել,
#    օրինակ՝ girls = [‘Ani’, ‘Gohar’, ‘Tatev’]
#            boys = [‘Gor’, ‘Vahe’, ‘Vardan’, ‘Karen’, ‘Ashot’]
#    - պատահականության սկզբունքով կտպի պարային զույգեր
#      list-երից փոքրագույն երկարություն ունեցողի քանակությամբ,
#    տվյալ օրինակի դեպքում կտպի՝ Gohar - Ashot
#                                Ani - Gor
#                                Tatev - Karen։

girls = ['Ani', 'Gohar', 'Tatev']
boys = ['Gor', 'Vahe', 'Vardan', 'Karen', 'Ashot']
c = 0
while c <= min(len(girls), len(boys)) + 1:
    g = random.choice(girls)
    b = random.choice(boys)
    girls.remove(g)
    boys.remove(b)
    c += 1
    print(g, '-', b)
