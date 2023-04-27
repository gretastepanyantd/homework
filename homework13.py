import random


# 1․ Գրել ծրագիր, որը․
#    - կսահմանի աստիճան բարձրացնելու ֆունկցիա power(x, y), որը կվերադարձնի x ի y աստիճանը,
#    - Եթե y չտրվի այդ ֆունկցիային` power(x), ապա ֆունկցիան պետք է վերադարձնի x ի 2 աստիճանը,
#    - հաշվի առեք բացառությունները։

def power(x, y=2):
    if x == y == 0:
        return 1
    elif x < 0 and type(y) == float and y % 1 != 0:
        return 'Result will be complex'
    elif type(x) in [int, float] and type(y) in [int, float]:
        return x ** y
    else:
        return 'Parameter\'s types must be integer or float.'


print(power(-16, 3))

# 2. Գրել զառ նետելու խաղի ծրագիր, որը․
#    - կպահի համակարգչի և խաղացողի հաշիվը,
#    - ցիկլի միջողոց՝
#      -- կկարդա խաղացողի կողմից մուտքագրված թիվը և կստուգի, որ այն լինի 1 - 6 սահմանում,
#      -- կգենեռացնի պատահական թիվ 1-6 սահմանում,
#      -- կորոշի, թե ով է հաղթողը և հաղթողի հաշիվը կավելացնի մեկով,
#    - խաղը ավարտվում է երբ համակարգչի կամ խաղացողիհաշիվը 5-ի է հասնում:

point_user = 0
point_computer = 0
while True:
    try:
        computer_version = random.randint(1, 6)
        user_version = int(input('Enter Number 1 to 6 ='))
        if user_version > 0 and user_version < 7 and user_version == computer_version:
            continue
        elif user_version > 0 and user_version < 7 and user_version > computer_version:
            point_user += 1
            if point_user == 5:
                print('WIN USER')
                break
        elif user_version > 0 and user_version < 7 and user_version < computer_version:
            point_computer += 1
            if point_computer == 5:
                print('WIN COMPUTER')
                break
        else:
            print('wrong input', 'must enter number 1 to 6 =', sep='\n')
    except ValueError:
        print('wrong input', 'must enter number 1 to 6 =', sep='\n')

# 3․ Գրել հետևյալ ծրագիրը․
#    - տրված բառարանը բաղկացած է տրանսպորտային միջոցներից և դրանց քաշից՝ կիլոգրամներով,
#    օրինակ՝ dict_1={"Sedan": 1500, "SUV": 2000,
#                    "Pickup": 2500, "Minivan": 1600,
#                    "Van": 2400, "Semi": 13600,
#                    "Bicycle": 12, "Motorcycle": 110},
#    - մեկ տողով կառուցեք 2 տոննայից ցածր քաշ ունեցող մեքենաների անունների
#      ցուցակը որպես list՝ բոլորի անունները մեծատառ դարձնելով,
#    - տվյալ օրինակի դեպքում կտպի`
#      ['SEDAN', 'MINIVAN', 'BICYCLE', 'MOTORCYCLE']

dict_1 = {'Sedan': 1500, 'SUV': 2000,
          'Pickup': 2500, 'Minivan': 1600,
          'Van': 2400, 'Semi': 13600,
          'Bicycle': 12, 'Motorcycle': 110}
name_list = [key.upper() for key in dict_1 if dict_1[key] < 2000]
print(name_list)
