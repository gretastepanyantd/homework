import math
import random

# 1․ Գրել ծրագիր, որը․
#    - input-ի միջոցով օգտատիրոջից կհարցնի աստիճան,
#    - կտպի այդ աստիճանին համապատասխան ռադիանը,
#    - կտպի sin ֆունկցիայի արժեքը այդ ռադիանում։

n = int(input('n='))
rad = math.radians(n)
sin = math.sin(rad)
print('radian=', rad, 'sin=', sin)

# 2. Գրել ծրագիր, որը․
#    - կգեներացնի 10 պատահական ամբողջ թիվ 10-ից 99 միջակայքում,
#    - այդ 10 թվերից պատահականորեն կընտրի 3 թիվ,
#    - կտպի այդ 3 թվերի միջին թվաբանականի քառակուսի արմատը։

c = 0
s = 0
a = random.sample(range(10, 100), 10)
b = random.sample(a, 3)
for i in b:
    s += i
    c += 1
print((s / c) ** 0.5)

# 3․ Գրել քար-թուղթ-մկրատ խաղի ծրագիր, որը․
#    - input-ի միջոցով օգտատիրոջից կհարցնի օգտատիրոջ ընտրած տարբերակը (քար, թուղթ կամ մկրատ),
#    - պատահակն ձևով կգեներացնի քար, թուղթ կամ մկրատ տարբերակներից մեկը,
#    - կհամեմատի օգտատիրոջ կողմից մուտքագրված տարբերակի հետ,
#    - կպահի խաղի հաշիվը,
#    - խաղը պետք է շարունակվի այնքան ժամանակ մինչև խաղացողներից մեկի հաշիվը կհասնի 5-ի,
#    - հաշիվը 5-ի հասնելուց հետո խաղը կավարտվի և կտպի հաղթողի անունը։

point_user = 0
point_computer = 0
while True:
    user_version = input('Enter Version-')
    computer_version = random.sample(['stone', 'paper', 'scissors'], 1)
    computer_version = computer_version[0]
    if user_version == 'stone' or user_version == 'paper' or user_version == 'scissors':
        if user_version == 'stone' and computer_version == 'scissors' or user_version == 'scissors' and \
                computer_version == 'paper' or user_version == 'paper' and computer_version == 'stone':
            point_user += 1
            if point_user == 5:
                print('WIN USER')
                break
        elif user_version == 'stone' and computer_version == 'paper' or user_version == 'scissors' and \
                computer_version == 'stone' or user_version == 'paper' and computer_version == 'scissors':
            point_computer += 1
            if point_computer == 5:
                print('WIN COMPUTER')
                break
    else:
        print('WRONG VERSION')
