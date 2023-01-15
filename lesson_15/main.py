# def hellow_world():  #обьявление функции
#     print("hello_world")
#
#
# hellow_world()  #вызов функции
#__________________________________________________________
# def plus(number1, number2):
#     result = number1 + number2
#     return result  #то что вернёт функция
#
# x = plus(5, 3)  #вызов функции с аргументом. результатзаписан в переменную
# plus(number2=3, number1=23)  #указание конкретных аргументов
#__________________________________________________________
# def is_anton(name):
#     if name == "антон":
#         return True
#
# if is_anton("Богбан"):  #если функция вернёт True
#     print("это антон")
# else:
#     print("это не антон")
#__________________________________________________________
# def is_sorted(list):
#     sorted2 = sorted(list)
#     if list == sorted2:
#         return True
#
# list = [1,2,3,4,5]
# if is_sorted(list):
#     print("список отсортирован по возрастанию")
# else:
#     print("список отсортирован")
#__________________________________________________________
# def find_longest(list):
#     listik2 = []
#     for i in list:
#         listik2.append(len(i))
#     maxy = max(listik2)
#     ind = listik2.index(maxy)
#     return list[ind],listik2[ind]
#
# listik = ["баран", "дома", "сидинт"]
#     for i in chisla:
#         if i > maxim:
#             maxim=i
#         elif i < mini:
#             mini =i
#
# print(find_longest(listik))
#__________________________________________________________
# def min_max(chisla):
#     mini = 0
#     maxim = 0
#     return maxim,mini
# chisla = [1.2,2,3,4.5,8]
# print(min_max(chisla))
#__________________________________________________________
# def is_prime(vnutr):
#     for i in range(2, vnutr+1):
#         if i == vnutr:
#             return True
#         if vnutr % i == 0:
#             break
# if is_prime(523):
#     print("победаааа")
# else:
#     print("нетттт")
#__________________________________________________________
# def join(spicock:list, razdelitel:str)->str:
#     resick = ""
#     for i in spicock:
#         resick += i + razdelitel
#     return resick
#
# listick = ["da", "net", "omlet"]
# print(join(listick, ">"))
#__________________________________________________________
# def factorial(chiclo):
#     x = 1
#     for i in range(2, chiclo+1):
#         x *= i  #произведение всех i
#     return x
# print(factorial(15))
















