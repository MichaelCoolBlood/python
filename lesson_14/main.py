#множества
# 1)повторения исключкны
#d1 = {"антон", "антон", "ЫЫЫЫ"}
# 2)неупорядочуные
#print(d1)
# 3)пустое множество это только set()
# 4)внутри только неизменяемые
#__________________________________________________________
# словари
# 1)изменяемый тип данных
# d = {
#     1: 1,
# }
# print(d)
# 3)пустой словарь = dict() или {}
#__________________________________________________________
#первый задача
# phrase = "маШа, ты гДе? Я теРМИтов лОмаю".lower()
# print(phrase)
# nejest = list("!,.?")
# cleared = ""
# d = {}
# for tagjikistan in phrase:
#     if tagjikistan not in nejest:
#         cleared += tagjikistan
# l = cleared.split(" ")
# print(l)
# for bogdan in l:
#     if bogdan not in d:
#         d[bogdan] = 1
#     else:
#         d[bogdan] += 1
# print(d)
#__________________________________________________________
#задада второй
# s = 0
# d = {"хлеб": 1000,
#      "молоко": 1.5,
#      "пол сырка": 47,
#      "елка": 50,
#      }
# #for price in d перебор по ключам
# for price in d.values():  #перебор по значениям
#     s += price
# print(s)
#__________________________________________________________
# 3)третий задача
# phrase = "маШа, ты гДе? Я маша я теРМИтов лОмаю".lower()
# print(phrase)
# nejest = list("!,.?")
# cleared = ""
# d = {}
# for tagjikistan in phrase:
#    if tagjikistan not in nejest:
#         cleared += tagjikistan
# l = cleared.split(" ")
# print(l)
# for bogdan in l:
#     if bogdan not in d:
#         d[bogdan] = 1
#     else:
#         d[bogdan] += 1
# print(d)
#
# maxi = max(d.values())
# for (key, values) in d.items():
#     if values == maxi:
#         print(f"ключ:{key}, значение:{values}")
#__________________________________________________________
#4) хороший кошьк
# d = {3:1,
#      9:2,
#      1:6,
#      "ключ1":2,
#      "еее":3,
# }
# one = 1
# two = 2
#
# one, two = two, one
# print(one, two)
#__________________________________________________________
d = {3:1,
     9:2,
     1:6,
     "ключ1":2,
     "еее":3,
}
d["еее"], d[3] = d[3], d["еее"]
print(d)

del d[9]
print(d)

d["new_key"] = "new_values"
print(d)































