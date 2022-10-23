# month = input("введи номер месяца:  ")
#
# if month.isdigit() and 1 <= int(month) <= 12:
#     month = int(month)
#     if 3 <= month <= 5:
#         print("весна")
#     elif 6 <= month <= 8:
#           print("лето")
#     elif 9 <= month <= 11:
#           print("осень")
#     else:
#           print("сима")
# else:
#     print("ок ты инопланетянин")
#_____________________________________________


# h = int(input("часы:  "))
# m = int(input("минуты:  "))
# s = int(input("секунды:  "))
#
# if 23 >= h >= 0 and 59 >= m >= 0 and 59 >= s >= 0:
#     print("Формат правильный :]")
#     print(f"{h}:{m}:{s}")
# else:
#     print("ошибка")
#     if h > 23 or h < 0:
#         print("часы в формате [0, 23]")
#     if m > 59 or m < 0:
#         print("минуты в формате [0, 59]")
#     if s > 59 or s < 0:
#          print("секунды в формате [0, 59]")
#_________________________________________________


score = 0
q1 = input("какого цвета трава?\n"
           "a)голубая, б)апельсин, в)60 бойцов, г)зелёная\n"
           "--> ")
if q1 == "г":
    score = score + 1
    print("праивино!")
else:
    print("ясбишо ыт")
    print("твой счёт: ", score)
    quit()

q2 = input("сколько ног у паука?\n"
           "а)шесть ,б)семь ,в)восемь ,г)девать\n"
           "-->")
if q2 == "в":
    score = score + 1
    print("праивино!")
else:
    print("ясбишо ыт")
    print("твой счёт: ", score)
    quit()

q3 = input("тунель какой длины может прорыть крот за ночь?\n"
           "а)76 ,б)8 ,в)100 ,г)150\n"
           "-->")
if q3 == "г":
    score = score + 1
    print("праивино!")
else:
    print("ясбишо ыт")
    print("твой счёт: ", score)
    quit()





























