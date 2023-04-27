# 1. Գրել, ծրագիր որը․
#    - կկարդա օգտագործողի կողմից մուտքագրված էլեկտրոնային փոստը,
#    - կստուգի արդյոք էլ․ փոստը ճիշտ է մուտքագրված
# (օրինակ՝ պարունակի @, պարունակի կետ, @-ից հետո հետո լինի կետ, ոչ անմիջապես և այլն)։

mail = input('mail-')
i1 = mail.index('@')
i2 = mail.index('.')
if '@' in mail and '.' in mail and i1 != 0 and i2 != 0 and i1 != len(mail) - 1 and i2 != len(
        mail) - 1 and i2 != i1 + 1 and i1 != i2 + 1:
    print(mail)
else:
    print('Invalid Email')

# 2. Գրել ծրագիր որը․
#    - կկարդա օգտագործողի կողմից մուտքագրված հեռախոսահամարը,
#    - կստուգի արդյոք հեռախոսահամարը ճիշտ է մուտքագրված (օրինակ կազմված լինի թվերից և այլն),
#    - կվերադարձնի հետևյալ ֆորմատով +374yyxxxxxx։

phonenumber = input('phonenumber-+374')
if phonenumber.isnumeric() and len(phonenumber) == 8:
    print(phonenumber)
else:
    print('invalid phonenumber')
