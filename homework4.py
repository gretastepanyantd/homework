# Գրել օնլայն-խանութի ծրագիր (while loop-ով)․
#    - ծրագիրը պետք է աշխատի միանիշ թվեր ընդունելով input ֊ի միջոցով
#    - օգտագործողը գրում է թվանշանը, ծրագիրը կատարում է կոնկրետ գործողություն
#      ու նորից input ի միջոցով սպասում է նոր թվանշանի օգտագործողի կողմից
#    - քանի դեռ օգտագործողը չի գրել “0” թվանշանը, որը ավարտի թվանշանն է,
#      ծրագիրը չպիտի ավարտվի,
#      ամեն գործողությունից հետո նորից պետք է input ի միջոցով կարդա նոր թվանշան
#    - ծրագիրը միացնելուց մեկ անգամ պետք է տպի թվանշանների նշանակության ցանկը՝
# ———————————————————————————————————————————————————————————————————————
# 0 - Exit
# 1 - Repeat this message
# 2 - Add one apple to cart (apple price is 1$)
# 3 - Remove one apple from cart
# 4 - Add one chocolate to cart (chocolate price is 3$)
# 5 - Remove one chocolate from cart
# 6 - Show my cart
# 7 - Show checkout information
# ———————————————————————————————————————————————————————————————————————
#    ● եթե օգտագործողը գրում է “0”, ապա ծրագիր պետք է տպի “Exit from shop” և ավարտվի
#    ● եթե օգտագործողը գրում է “1” ապա պետք է տպի թվանշանների
#       նշանակության ցանկը (որը ցուցադրված է վերևում)
#    ● եթե օգտագործողը գրում է “2” ապա պետք է խնձորների քանակը
#       մեկով մեծացնենք(խնձորների քանակը սկզբից 0 է)
#    ● եթե օգտագործողը գրում է “3” ապա պետք է խնձորների քանակը
#       մեկով քչացնենք(ստուգելով եթե խնձորների քանակը մեծ է 0-ից,
#       հակառակ դեպքում ուղղակի թողնում ենք 0)
#    ● եթե օգտագործողը գրում է “4” ապա պետք է շոկոլադների քանակը
#       մեկով մեծացնենք(շոկոլադների քանակը սկզբից 0 է)
#    ● եթե օգտագործողը գրում է “5” ապա պետք է շոկոլադների քանակը
#       մեկով քչացնենք(ստուգելով եթե շոկոլադների քանակը մեծ է 0-ից,
#       հակառակ դեպքում ուղղակի թողնում ենք 0)
#    ● եթե օգտագործողը գրում է “6” ապա պետք է տպենք թե քանի
#       խնձոր և քանի շոկոլադ ունի նա զամբյուղում
#    ● եթե օգտագործողը գրում է “7” ապա պետք է ցույց տանք թե քանի դոլար
#       նա պետք է վճարի (մեկ խնձորը արժի մեկ դոլար, իսկ մեկ շոկոլադը՝ երեք դոլար)։

print('1 - Repeat this message', '2 - Add one apple to cart (apple price is 1$)', '3 - Remove one apple from cart',
      '4 - Add one chocolate to cart (chocolate price is 3$)', '5 - Remove one chocolate from cart',
      '6 - Show my cart', '7 - Show checkout information', '0-Exit from shop', sep='\n')

count_apple = 0
count_chocolate = 0
a = 0
c = 0
total_price = 0

while True:
    command = input('command=')
    if command == '1':
        print('1 - Repeat this message', '2 - Add one apple to cart (apple price is 1$)',
              '3 - Remove one apple from cart',
              '4 - Add one chocolate to cart (chocolate price is 3$)', '5 - Remove one chocolate from cart',
              '6 - Show my cart', '7 - Show checkout information', '0-Exit from shop', sep='\n')
    elif command == '2':
        count_apple += 1
    elif command == '3':
        if count_apple > 0:
            count_apple -= 1
        else:
            count_apple = 0
    elif command == '4':
        count_chocolate += 1
    elif command == '5':
        if count_chocolate > 0:
            count_chocolate -= 1
        else:
            count_chocolate = 0
    elif command == '6':
        print(f'count_apple- {count_apple},count_chocolate- {count_chocolate}', sep='\n')
    elif command == '7':
        a = count_apple * 1
        c = count_chocolate * 3
        total_price = a + c
        print(total_price)
    elif command == '0':
        print('Exit from shop')
        break
    else:
        print('wrong command')
