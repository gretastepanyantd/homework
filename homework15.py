import time


# 1․ Գրել ֆունկցիա, որը․
#    - կստանա արգումենտ մեքենայի արագությունը մղոն/ժամ,
#    - կվերադարձնի մեքենայի արագությունը կմ/ժամ։


def speed(v1):
    if (type(v1) == float or type(v1) == int) and v1 > 0:
        v2 = v1 * 1.609344       # 1.609344 - ցամաքային մղոնի արժեքը։
        return v2
    return 'must enter a positive number'


print(speed(100))


#  2. Գրել ֆունկցիա, որը․
#    - կհաշվի 1-ից 10000 միջակայքում գտնվող 3-ի բաժանվող թվերի քանակը,
#    - կտպի այդ ֆունկցիայի կատարման ժամանակը վայրկյաններով։

def divide_into_three():
    count = 0
    for i in range(1, 1000001, 3):      #Թիվը մեծացրել եմ, որովհետև 10000-ով 0.0 էր ստացվում։
        count += 1
    return count


t1 = time.time()
divide_into_three()
t2 = time.time()
print(t2 - t1)

# 3․ Գրել ծրագիր, որը․
#    - կունենա թվերից բաղկացած list,
#    - list-ը կբաժանի 2 list-երի այնպես,
#      որ առաջին list-ում կլինեն նախնական list-ի առաջին, երրորդ, հինգերորդ և այլն էլեմենտները,
#      իսկ երկրորդ list-ում՝ երկրորդ, չորորդ, վեցերորդ և այլն էլեմենտները,
#    - կհաշվի և tuple-ով կտպի այդ list-երի միջին թվաբանականները,
#    օրինակ՝ list_1 = [50, 60, 60, 45, 70]
#    պետք է ստացվի՝ (60, 52.5):

list_1 = [50, 60, 60, 45, 70]
even_index_list = []
odd_index_list = []
for j in range(len(list_1)):
    if j % 2 == 0:
        even_index_list.append(list_1[j])
    else:
        odd_index_list.append(list_1[j])
tuple_1 = (sum(even_index_list) / len(even_index_list), sum(odd_index_list) / len(odd_index_list))
print(tuple_1)
