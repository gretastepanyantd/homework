# 1. Գրել ծրագիր, որը․
#    - մեկ տողով կստեղծի նոր dictionary հետևյալ dictionary-ից և list-ից,
#    sample_dict = {"name": "Kelly",
#                   "age": 25,
#                   "salary": 8000,
#                   "city": "New york"},
#    keys = ["name", "salary"],
#    արդյունքում պետք է ստացվի․
#    {'name': 'Kelly', 'salary': 8000}:

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
keys = ["name", "salary"]
new_dict = {k: sample_dict[k] for k in keys}
print(new_dict)

# 2. Գրել ծրագիր, որը․
#    - կտպի Մայքի պատմության գնահատականը հետևյալ dictionary-ից՝
#    sampleDict = {"class A": {"student_1": {"name": "Mike",
#                                            "marks": {"physics": 70,
#                                                      "history": 80}}
#                              "student_2": {"name": "Jack",
#                                            "marks": {"physics": 80,
#                                                      "history": 75}}}}

sampleDict = {"class A": {"student_1": {"name": "Mike",
                                        "marks": {"physics": 70,
                                                  "history": 80}},
                          "student_2": {"name": "Jack",
                                        "marks": {"physics": 80,
                                                  "history": 75}}}}
print(sampleDict["class A"]["student_1"]["marks"]["history"])

# 3. Գրել ծրագիր, որը․
#    - կմիավորի երկու dictionary-ները այնպես, որ ստացված dictionary-ում պահպանվի նույն key ունեցողների ամենամեծ value-ն,
#    օրինակ՝ dict1 = {'d': 50, 'a': 10, 'b': 20, 'c': 30},
#            dict2 = {'b': 30, 'a': 5, 'd': 25, 'c': 20},
#            արդյունքում պետք է ստացվի․
#            {'b': 30, 'a': 10, 'd': 50, 'c': 30}։

dict1 = {'d': 50, 'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 30, 'a': 5, 'd': 25, 'c': 20}
for k in dict1:
    if dict1[k] < dict2[k]:
        dict1[k] = dict2[k]
print(dict1)
