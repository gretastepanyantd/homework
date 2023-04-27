import os

# 1․ Գրել ծրագիր, որը․
#    - միացնելուց պետք է ստուգի usernames.txt ֆայլի առկայությունը (հիշեք անցած մոդուլներից),
#    - եթե ֆայլը առկա է, պետք է կարդա ֆայլում գրաված անունները և պահի usernames լիստում,
#    - եթե ֆայլը առկա չէ, պետք է ստեղծի դատարկ usernames լիստ,
#    - պետք է տպի թվանշանների նշանակության ցանկը՝
#      0 - Save to file
#      1 - Add user name
#    - ցիկլի մեջ
#      -- կարդա input()՝ մարդու կողմից մուտքագրած թիվը,
#      -- եթե թիվը 1 է, ապա կարդա input() մարդու կողմից ավելացված անունը
#         և ավելացնի usernames լիստին,
#      -- եթե թիվը 0 է, ապա կգրի usernames լիստը usernames.txt ֆայլի մեջ։

file = 'usernames.txt'
if os.path.exists(file):
    file = open('usernames.txt', 'r')
    usernames = file.readlines()
    usernames = list(map(lambda x: x[:-1], usernames))
    file.close()
    print('0 - Save to file', '1 - Add user name', sep='\n')
else:
    usernames = []
while True:
    number = input('0 or 1 - ')
    if number == '1':
        name = input('Add user name - ')
        usernames.append(name)
    elif number == '0':
        file = open('usernames.txt', 'w')
        for i in usernames:
            file.write(i + "\n")
        print(usernames)
        file.close()
        break


# 2․ Գրել ռեկուրսիվ ֆունկցիա, որը․
#    - կգտնի ոչ բացասական թվի թվանշանների գումարը,
#    օրինակ՝ 285 -> 15։

def sum_of_number_rec(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_number_rec(n // 10)


print(sum_of_number_rec(123))

# 3․ Գրել ծրագիր, որը․
#    - կկարդա որևէ տեքստային ֆայլ,
#    - կհաշվի թե քանի անգամ է հանդիպում այդ ֆայլի մեջ Python բառը և կտպի այդ քանակը,
#    - կտպի բոլոր այն տողերի համարները, որտեղ կա Python բառը,
#    - բոլոր "Python" բառերը ֆայլի մեջ կփոխարինի "Machine learning" բառակապակցությամբ,
#    - կպահպանի ֆայլը։

line_num = 0
line_num_list = []
count_Python = 0
sch_word = 'Python'
rep_word = 'Machine learning'
new_data = []

with open('python language.txt') as file:
    for line in file.readlines():
        line_num += 1
        if sch_word in line:
            line_num_list.append(line_num)
            count_Python += line.count(sch_word)
            new_data.append(line.replace(sch_word, rep_word))
        else:
            new_data.append(line)

f2 = open('python language.txt', 'w')
f2.writelines(new_data)
f2.close()

print('Count:', count_Python)
print('Numbers of lines:', line_num_list)
