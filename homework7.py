# 1 Write a Python program to convert a given tuple of tuples to a list of lists with list
# comprehension.

tuple1 = ((1, 2), (2, 3), (3, 4))
a = [list(elem) for elem in tuple1]
print('list=', a)

# 2. Գրել ծրագիր, որը․
#    - կտպի հետևյալ tuple-ների էլեմենտ առ էլեմենտ գումարը,
#    օրինակ՝ tuple_1 = (1, 2, -3, 4),
#            tuple_2 = (3, 5, 2, 1),
#            tuple_3 = (2, -2, 0, 1),
#            արդյունքը պետք է լինի՝
#            (6, 5, -1, 6)։

tuple_1 = (1, 2, -3, 4)
tuple_2 = (3, 5, 2, 1)
tuple_3 = (2, -2, 0, 1)
tuple_4 = []
for i in range(0, len(tuple_1)):
    tuple_4.append(tuple_1[i] + tuple_2[i] + tuple_3[i])
print('sum tuple=', tuple(tuple_4))

# 3. Գրել ծրագիր, որը․
#    - կտպի tuple-ներից բաղկացած list-ի բոլոր էլեմենտների գումարը,
#    օրինակ՝ list1 = [(1, 2, 6), (2, 3, -6), (3, 4), (2, -6, 2, 8)],
#            արդյունքը պետք է լինի՝
#            21:

list1 = [(1, 2, 6), (2, 3, -6), (3, 4), (2, -6, 2, 8)]
s = 0
for i in list1:
    for j in i:
        s += j
print(s)

# 4. Գրել ծրագիր, որը․
#    - երկու չկրկնվող էլեմենտներ պարունակող list-երից կվերցնի բոլոր այն էլեմենտները,
#      որոնք կան և առաջինի մեջ, և երկրորդի ու կվերադարձնի սորտավորված այդ էլեմենտները tuple-ի տեսքով,
#    օրինակ՝ list_1 = [12, 41, 5, 8, 0, 11, -7, 9, -1],
#            list_2 = [36, -12, 0, 18, -1, 12, 45, 21],
#            արդյունքը պետք է լինի՝
#            tuple_1 = (-1, 0, 12)։

list_1 = [12, 41, 5, 8, 0, 11, -7, 9, -1]
list_2 = [36, -12, 0, 18, -1, 12, 45, 21]
list_3 = []
for i in list_1:
    if i in list_2:
        list_3.append(i)
print(tuple(list_3))

# 5. Գրել ծրագիր, որը․
#    - կտպի tuple_5 ի միջի թվային արժեքների միջին թվաբանականի քառակուսին․
#      tuple_1 = (11, "55", 54, “abc”, 90, 102, “asdasd”, “qwerty”):

tuple_5 = (11, '55', 54, 'abc', 90, 102, 'asdasd', 'qwerty')
s = 0
c = 0
for i in tuple_5:
    if str(i).isdigit():
        s += int(i)
        c += 1
print((s / c) ** 2)
