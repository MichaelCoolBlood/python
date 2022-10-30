# try:
#     number = int(input("введи число:  "))
#
#     x = 5 / number
#     print(x)
# except ZeroDivisionError:
#     print("на ноль ты не делиииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииии")
# except ValueError:
#     print("хачу цифирки")
# except Exception:
#     print("одна ошибка и ты ошився")
#_____________________________________________________________


# try:
#     name = input("введи имя:  ")
#     if name == "антон":
#         raise Exception("это имя под запретом")
# except Exception as error_m:
#     print("ненядя", error_m)
# else:
#     print("ну вот такое имя можно")
# finally:
#     print("Ы")
#
# print("смена окончена")
#_______________________________________________________-


# try:
#     number = int(input("введи число:  "))
#     x = 5 / number
# except Exception:
#     pass
#
# if 3 == 3:
#     pass  # TODO: не забуть написать и купить молока.



def summa(numbers):
    return sum(numbers)

print(summa([1, 2, 3]))
assert summa([1, 2]) == 3
assert summa([1, 2]) == 4
















