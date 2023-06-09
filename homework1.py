# 1. Գրել, ծրագիր որը․
#    - կկարդա օգտագործողի կողմից մուտքագրված x փոփոխականը (input-ի միջոցով),
#    - կկարդա օգտագործողի կողմից մուտքագրված y փոփոխականը (input-ի միջոցով),
#    - կտպի x-ի և y-ի գումարը,
#    - կտպի x-ի և y-ի տարբերությունը,
#    - կտպի x-ի և y-ի արտադրյալը,
#    - կտպի x-ի և y-ի քանորդը,
#    - կտպի x-ի և y-ի քանորդի ամբողջ մասը,
#    - կտպի x-ի և y-ի քանորդի մնացորդային մասը,
#    - կտպի x-ը բարձրացրած y աստիճան։

x = float(input(' x='))
y = float(input('y='))
print(x + y, x - y, x * y, x / y, x // y, x % y, x ** y)

# 2. Գրել ծրագիր, որը․
#    - կկարդա օգտագործողի կողմից մուտքագրված անունը (input-ի միջոցով),
#    - կկարդա օգտագործողի կողմից մուտքագրված ազգանունը (input-ի միջոցով),
#    - կկարդա օգտագործողի կողմից մուտքագրված տարիքը (input-ի միջոցով),
#    - կտպի հետևյալը․ "Hello {անուն} {ազգանուն}. You are {տարիք} years old.":

name = input('name-')
surname = input('surname-')
age = int(input('age-'))
print('Hello', name, surname, 'You are', age, 'years old.')

# 3. Գրել ծրագիր որը։
#    - կկարդա օգտագործողի կողմից մուտքագրված age փոփոխականը (input֊ի միջոցով),
#    - եթե age փոքր լինի 18 ից կտպի “you are under 18”, հակառակ դեպքում կտպի “you are over 18”․

age = int(input('age-'))
if age < 18:
    print('You are under 18.')
elif age == 18:
    print('You are 18 years old.')
else:
    print('You are over 18.')

# 4. Գրել ծրագիր, որը․
#    - կկարդա օգտագործողի կողմից մուտքագրված a պարամետրը (input-ի միջոցով),
#    - կկարդա օգտագործողի կողմից մուտքագրված b պարամետրը (input-ի միջոցով),
#    - կկարդա օգտագործողի կողմից մուտքագրված c պարամետրը (input-ի միջոցով),
#    - կլուծի a*x^2 + b*x + c = 0 քառակուսային եռանդամը և կտպի x1 և x2 լուծումները
#      (D = b^2 - 4*a*c, եթե D > 0, ապա x1 = (-b + sqrt(D)) / (2 * a), x2 = (-b - sqrt(D)) / (2 * a),
#                        եթե D = 0, ապա x = - b / (2 * a),
#                        եթե D < 0, ապա իրական թվերի բազմության մեջ լուծում չունի)։

a = float(input('a='))
b = float(input('b='))
c = float(input('c='))
D = b ** 2 - (4 * a * c)
if D > 0:  # (x2−6x+5=0)
    x1 = (-b + (D ** 0.5)) / (2 * a)
    x2 = (-b - (D ** 0.5)) / (2 * a)
    print(x1, x2)  # (5,1)
elif D == 0:  # (25x2−10x+1=0)
    x = -b / (2 * a)
    print(x)  # (0.2)
else:  # (3x2−5x+4=0)
    print('R has no native solution')
