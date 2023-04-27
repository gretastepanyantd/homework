# 1․ Գրել ծրագիր որը․
#    - կունենա ֆունկցիա is_prime անունով, որը կստանա ամբողջ թիվ
#      և կվերադարձնի True եթե թիվը պարզ է, հակառակ դեպքում կվերադարձնի False,
#    - օգտագործել is_prime և filter ֆունկցաները` ստանալ 1-ից մինչև 1000 միջակայքում
#      գտնվող պարզ թվերի list,
#    - տպել տվյալ list-ը։

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


prime_list = list(filter(is_prime, range(1, 1001)))
print(prime_list)

# 2. Գրել ծրագիր, որը․
#    - կունենա սահմանված երկու list-եր,
#      nums_1 = [1, 2, 3, 5, 7, 8, 9, 10],
#      nums_2 = [1, 2, 4, 8, 9],
#    - կստեղծի list, որը բաղկացած կլինի այն թվերից,
#      որոնք կան և nums_1 ի, և nums_2 ի մեջ օգտագործելով filter և lambda,
#    - կտպի ստացված լիստը,
#    տվյալ օրինակում պետք է տպի՝ [1, 2, 8, 9]։

nums_1 = [1, 2, 3, 5, 7, 8, 9, 10]
nums_2 = [1, 2, 4, 8, 9]
nums_3 = list(filter(lambda x: x in nums_1, nums_2))
print(nums_3)

# 3․ Գրել ծրագիր, որը․
#    - կունենա dict-երից բաղկացած list,
#    օրինակ՝ user_list = [{'name': 'Arman', 'age': 23},
#                         {'name': 'Bob', 'age': 19},
#                         {'name': 'Anna', 'age': 21}],
#    - կսորտավորի list-ի էլեմենտները ըստ ‘age’-ի sort ֆունկցիային փոխանցելով lambda ֆունկցիա,
#    - կտպի ստացված dictionary-ների list-ը,
#    տվյալ օրինակում պետք է տպի՝ [{'name': 'Bob', 'age': 19},
#                                 {'name': 'Anna', 'age': 21},
#                                 {'name': 'Arman', 'age': 23}]։

user_list = [{'name': 'Arman', 'age': 23},
             {'name': 'Bob', 'age': 19},
             {'name': 'Anna', 'age': 21}]
user_list.sort(key=lambda a: a['age'])
print(user_list)
