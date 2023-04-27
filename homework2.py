# 1. Գրել, ծրագիր որը․
#    - կկարդա օգտագործողի կողմից մուտքագրված text փոփոխականը (input-ի միջոցով),
#    - կտպի text-ի առաջին և վերջին տառերը,
#    - կտպի text-ի մեջտեղի տառը։

text = input('text-')
print(text[0], text[-1])
print(text[len(text) // 2])

# 2. Գրել ծրագիր որը․
#    - կկարդա օգտագործողի կողմից մուտքագրված text փոփոխականը (input֊ի միջոցով),
#    - եթե text-ի երկարությունը զույգ թիվ է, կպտի text-ի առաջին կեսը,
#    - եթե text-ի երկարությունը կենտ է, կտպի մեջտեղում գտնվող սիմվոլը:
#    Օրինակներ՝
#      cat - բառի համար տպի a,
#      door - բառի համար տպի do։

text = input('text-')
if len(text) % 2 == 0:
    print(text[0:len(text) // 2])
else:
    print(text[len(text) // 2])

# 3․ Գրել ծրագիր, որը․
#    - կկարդա օգտագործողի կողմից մուտքագրված text փոփոխականը (input֊ի միջոցով),
#    - կստուգի արդյոք text-ը սկսվում է մեծատառով,
#    - կստուգի արդյոք text-ը սկսվում է փոքրատառով,
#    - կստուգի արդյոք text-ի երկարությունը զույգ է, թե կենտ, և կտպի արդյունքը,
#    - կստուգի թե քանի անգամ է ՛a՛ տառը կրկնվում text-ի մեջ և կտպի այդ թիվը,
#    - կստուգի արդյոք text-ի բոլոր սիմվոլները տառեր են,
#    - կդարձնի text-ի բոլոր տառերը փոքրատառ,
#    - կդարձնի text-ի առաջին տառը մեծատառ,
#    - կգտնի ՛a՛ տառի ինդեկսը text-ի մեջ,
#    - կփոխարինի text-ի մեջ հանդիպած առաջին ՛a՛ տառը ՛b՛ տառով,
#    - կավելացնի 5 զրոներ text-ի և աջ, և ձախ կողմերից։

text = input('text-')
print(text[0].istitle())
print(text[0].islower())
c = text.count('a')
print(c)
print(text.isalpha())
print(text.lower())
print(text.capitalize())
print(text.index('a'))
text1 = text.replace('a', 'b', 1)
print(text1)
print(text.ljust(5 + len(text), '0'))
print(text.rjust(5 + len(text), '0'))
if len(text) % 2 == 0:
    print('even')
else:
    print('odd')

# 4․ Գրել ծրագիր, որը․
#    - կկարդա օգտագործողի կողմից մուտքագրված անունը (input-ի միջոցով),
#    - կկարդա օգտագործողի կողմից մուտքագրված ազգանունը (input-ի միջոցով),
#    - կկարդա օգտագործողի կողմից մուտքագրված տարիքը (input-ի միջոցով),
#    - օգտագործելով f-string կտպի հետևյալը․ "Hello {անուն} {ազգանուն}. You are {տարիք} years old.":

name = input('name-')
surname = input('surname-')
age = int(input('age-'))
text = f'Hello {name} {surname}. You are {age} years old.'
print(text)
