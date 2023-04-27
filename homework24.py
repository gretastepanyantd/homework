# 1․ Գրել ֆունկցիա, որը․
# - տրված բառերի list - ը max_len_words(["aba", "aa", "z", "ad", "vcd", "aba"])
# (այսինքն՝ կգտնի ամենաերկար բառի երկարությունը և լիստում կթողնի միայն այդ երկարության բառերը),
# օրինակ՝ input = ["aba", "aa", "z", "ad", "vcd", "aba"]
# output = ["aba", "vcd", "aba"],
# input = ["aba", "aa", "z", "advc", "vcd", "aba"]
# output = ["advc"],
# - վերջում գնահատեք Ձեր գրած կոդը Big O notation - ի միջոցով։

def max_len_words(word_list):
    max_len = max(word_list, key=len)
    word_list = list(filter(lambda x: len(x) == len(max_len), word_list))
    return word_list


print(max_len_words(["aba", "aa", "z", "ad", "vcd", "aba"]))


# 2․ Գրել ֆունկցիա, որը․
# - կհաշվի, թե տրված ամբողջ թվերի list - ից քանի քայլով կարելի է ստանալ մոնոտոն աճող թվերից բաղկացած list, մեկ քայլի
# ընթացքում թույլատրվում է թվերից մեկը  մեկով մեծացնել, թվերի տեղերը փոխել չի կարելի,
# օրինակ՝ [-10, 0, -2, 0] -> 5,
# [1, 1, 1] -> 3:


def monotonic_step(l_1):
    step_count = 0
    for i in range(0, len(l_1) - 1):
        if l_1[i] >= l_1[i + 1]:
            step_count += l_1[i] - l_1[i + 1] + 1
            l_1[i + 1] += l_1[i] - l_1[i + 1] + 1
    return step_count


print(monotonic_step([-10, 0, -2, 0]))


# 3. Գրել ֆունկցիա, որը․
# - կստանա երկու արգումենտ՝ a և b,
# - կվերադարձնի a - ի b աստիճանի ամենավերջի թվանշանը, փորձել խնդիրը լուծել այնպես, որ կոդը աշխատի շատ արագ՝
# նույնիսկ շատ մեծ թվերի դեպքում։

def last_digit(a, b):
    if a == 0 and b == 0:
        return 1
    elif b == 0:
        return 1
    elif a == 0:
        return 0
    elif b % 4 == 0:
        res = 4
    else:
        res = b % 4

    num = (a ** res) % 10
    return num


print(last_digit(137, 5))


# 4. Caesar cipher

def caesar_cipher(text):
    caesar_cipher_text = ""
    for i in text:
        char = i
        if char.isupper():
            caesar_cipher_text += chr((ord(char) + 3 - 65) % 26 + 65)
        else:
            caesar_cipher_text += chr((ord(char) + 3 - 97) % 26 + 97)
    return caesar_cipher_text


print("Caesar cipher text - " + caesar_cipher("Greta"))
