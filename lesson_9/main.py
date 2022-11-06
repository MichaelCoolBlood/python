# import random
# import time
#
# print("время пострелять.")
#
# is_game = "y"
# while is_game == "y":
#     time.sleep(1.5)
#     print("*заряжаем револьвер*")
#     time.sleep(2.5)
#     print("*раскручиваем барбабан")
#     time.sleep(1)
#     print(3)
#     time.sleep(1)
#     print(2)
#     time.sleep(1)
#     print(1)
#     time.sleep(1)
#     print("выстрел")
#
#     slots = [1, 2, 3, 4, 5, 6,]
#     patron = random.choice(slots)
#     our = random.choice(slots)
#
#     if patron == our:
#         print("теперь ветер в голове гуляет")
#         is_game = "n"
#     else:
#         print("ты жыв")
#         x = input("играем дальше? y - да, n - нет")
#         if x ==  "n":
#             is_game = "n"
# __________________________________________________

#циклы

#for
# lst = ["антон1", "антон2", "антон3", "антон4", "антон5"]
# for anton in lst:
#     print(anton, end="🕸")
#
# print()
# for i in range(0, 10):
#     print("питон т")
#
# #while
# x = 0
# while x != 10:
#     print(x)
#     x += 1
# ________________________________________

# word = input("введи слово:  ")
# while word:
#     print(word)
#     word = word[:-1]
#_________________________________________

# x = int(input("введи цифирю:  "))
# while x:   #если не равно 0, то рвботает
#     x -= 1  #то же самое что и x = x - 1
#     if x % 2 == 0:
#         print(x, end=" ")
# ________________________________________

# x = int(input("введи цифирю:  "))
# step = 0
# while x != 1:
#     step += 1
#     if x % 2 == 0:
#         print(f"{step})", end=" ")
#         print(x, "* 3 + 1 =", end=" ")
#         x = x // 2
#         print(x)
#     else:
#         print(f"{step})", end=" ")
#         print(x, " / 2 =", end=" ")
#         x = 3 * x + 1
#     print(x)
# print("шагов:", step)












