# primer1 = lambda a, b: a + b + 1  #лямбда функцию поместили в переменную
#
# print(primer1(5, 10))  #вызов функции не отличается
#
# answer = "д"
# exit_triger = lambda yn: True if yn == "д" else False
# print(exit_triger(answer))
#__________________________________________________________
#гененратор списка(list comprehesion)
# lst = []
# for i in range(1, 6):
#     lst.append(i)
# print(lst)
#
# lst2 = [i for i in range(1, 6)]  #!!!!!!!!!!!!!!!!!!!
#1. всгда майенкравтовские скобки
#2. for i in ... -> сколько элементов в списке
#3. всё что перед for -> сам элемент списка
#__________________________________________________________
# за дачей 1 малина
# c2f = lambda c: 9/5 * c + 32
# f2c = lambda f: (f-32)* 5/9
# c2k = lambda c: 273.15 + c
# k2c = lambda k: k - 273.15
# f2k = lambda f: c2k(f2k(f))
#__________________________________________________________
# import random
# exit_vihod = lambda yn: True if yn == "д" else False
# while True:
#     kub = int(input("сколько кубиков бросаем?"))
#     dices = [random.randint(1, 6) for i in range(kub)]
#     print(dices)
#     igrok = input ("хочеш ли ты выйти? да-д | нет-н: ")
#     print(exit_vihod(igrok))
#     if exit_vihod(igrok) == True:
#          break
#__________________________________________________________
# from random import choice
# chars = [list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"),
#          list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя"),
#          list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
#          list("abcdefghijklmnopqrstuvwxyz"),
#          list("1234567890")
#         ]
# lst = []
# for i in range(6):
#     lst.append(choice(choice(chars)))
# code = "".join(lst)
# ssilka = "https://youtu.be/iEFc-Si7zd8"
# d = {"https://youtu.be/iEFc-Si7zd8" : "fyflo"}
# d = {}
# if ssilka in d:
#     print("эта ссылка уже есть в базе вот её код ->", d[ssilka])
# else:
#     d[ssilka] = code
#     print("ссылка добавлена вот её код->", d[ssilka])
#__________________________________________________________
# import math
#
# a = 2
# b = 1024
# yy1 = lambda a, b : b - a
# print(yy1(a, b))
#
# yy2 = lambda a, b : b + a
#
# yy3 = lambda a, b : b /a
#
# yy4 = lambda a, b: b * a
#
# yy5 = lambda a, b: a / b
#
# acb = lambda x : -x if x<0 else x
# print((acb(-5)))
#
# logarifm = lambda a, b : math.log(b, a)
# print(logarifm(16, 2))













