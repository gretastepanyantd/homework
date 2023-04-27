# 1. Գրել ծրագիր, որը․
#    - dictionary-ի key-երի միջից կջնջի բոլոր բացատները,
#    օրինակ՝ {'S  001': ['Math', 'Python'], ' S    002': ['Math', 'English']},
#            պահանջվող արդյունքը՝
#            {'S001': ['Math', 'Science'], 'S002': ['Math', 'English']}:

dict1 = {'S  001': ['Math', 'Python'], ' S    002': ['Math', 'English']}
dict1 = {i.replace(' ', ''): j
         for i, j in dict1.items()}
print(dict1)

# 2. Գրել ծրագիր, որը․
#    - կտպի dictionary-ի երեք ամենամեծ value ունեցող key-երը իրենց value-ներով,
#    օրինակ՝ {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24},
#            պահանջվող արդյունքը՝
#            item4 = 55,
#            item1 = 45.5,
#            item3 = 41.3:

dict2 = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}
v = list(dict2.values())
v.sort(reverse=True)
v = v[:3]
for i in v:
    for j in dict2.keys():
        if dict2[j] == i:
            print(str(j) + " = " + str(dict2[j]))

# 3. Գրել ծրագիր, որը․
#    - գտնել հետևյալ list-ի price-ների գումարը,
#    օրինակ՝ fruits = [{'fruit': 'orange', 'price': 150},
#                      {'fruit': 'apple', 'price': 100},
#                      {'fruit': 'banana', 'price': 200}],
#            պահանջվող արդյունքը՝
#            450:

fruits = [{'fruit': 'orange', 'price': 150},
          {'fruit': 'apple', 'price': 100},
          {'fruit': 'banana', 'price': 200}]
s = 0
for i in fruits:
    s += i.get('price')
print(s)
