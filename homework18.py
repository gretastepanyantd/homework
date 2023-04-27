# 1․ Գրել ծրագիր, որը․
# - կհաշվի դրական ամբողջ թվի ֆակտորիալը օգտագործելով ռեկուրսիա:

def rec_factorial(n):
    if n == 1:
        return 1
    return n * rec_factorial(n - 1)


print(rec_factorial(5))

# 2․ Գրել ռեկուրսիվ ֆունկցիա, որը․
# - կգտնի հետևյալ list - ի բոլոր էլեմենտների գումարը ռեկուրսիայի միջոցով առանց sum ֆունկցիա օգտագործելու,
# օրինակ՝ [1, 2, [3, 4], [5, [6, 7]]]

list_1 = [1, 2, [3, 4], [5, [6, 7]]]


def rec_sum(list1):
    s = 0
    for i in list1:
        if not isinstance(i, list):
            s += i
        else:
            s += rec_sum(i)
    return s


print(rec_sum(list_1))


# 3․ Գրել հետևյալ ծրագիրը․
# -------------------------------------
#   -----------------------------
# def decorator_example(func):
#     ...

# @decorator_example
# def print_avg(x):
#     print(sum(x) / len(x))
#
#
# print_avg([4, 5, 9])
# --------------------------
#   ----------------------------------------
#
# - print_avg ֆունկցիան տպում է տրված լիստի միջին թվաբանականը (այս ֆունկցիան չպիտի փոխենք),
# - գրել decorator_example ֆունկցիայի “․․․” ի փոխարեն կոդն այնպես, որ print_avg֊ֆունկցիան կանչելուց տպի նաև՝
# - լիստի էլեմենտների գումարը,
# - լիստի էլեմենտների քանակը,
# - արդյունքում կոդը պետք է[4, 5, 9] լիստի դեպքում տպի՝
#                             18
#                             3
#                             6.0

def decorator_example(func):
    def inner(x):
        func(x)
        print(sum(x), len(x), sep='\n')

    return inner


@decorator_example
def print_avg(x):
    print(sum(x) / len(x))


print_avg([4, 5, 9])
