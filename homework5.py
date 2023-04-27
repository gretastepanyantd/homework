# 1. Գրել, ծրագիր որը․
#    - կհաշվի դրական թվի թվանշանների գումարը,
#    օրինակ՝ 1456 ի դեպքում 1+4+5+6 = 16։

n = int(input('n='))
s = 0
while n != 0:
    s += (n % 10)
    n = n // 10
print(s)

# 2․ Գրել ծրագիր որը․
#    - կկարդա count թիվը (input- ի միջոցով),
#    - count քանակով թիվ կկարդա (input- ի միջոցով),
#    - կտպի այդ թվերի միջին թվաբանականը,
#    օրինակ՝ Type count: 4,
#            Type number: 10,
#            Type number: 25,
#            Type number: 35,
#            Type number: 30,
#            Result is 25։

count = int(input('count='))
a = 0
s = 0
while True:
    n = int(input('n='))
    s += n
    a += 1
    if a == count:
        print(s / count)
        break

# 3. Գրել ծրագիր որը․
#    - կգտնի մուտքագրված թվից մեծ ամենափոքր այն թիվը, որը հանդիսանում է բնական թվի քառակուսի,
#    օրինակ՝
#    num = 5     # result is 9,
#    num = 50    # result is 64,
#    num = 122   # result is 144։

num = int(input('num='))
print(int((num ** 0.5) + 1) ** 2)
