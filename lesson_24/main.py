# class human:
#     def __init__(self):  #инициализация
#         self.height = 993  #public данные
#         self.__money = 0.2  #private данные
#
#
#     def zdarova(self):  #обычный
#        return "усилено приветствую"
#
#     def ipotek(self):
#         if self.__money > 50 and self.height():  #юзаем private (внутри класса)
#             return True
#         else:
#             return "попрошу у мамы или у людей на Маркса"
#     def __normal_height(self):
#         if 100 <self.height < 200:
#             return True
#
# chelovek = human()
# #print(chelovek.height)
# # print(zdarova())
#
# print(chelovek.height)  #public можно выводить
# chelovek.height += 7  #public можно менять
#
# #print(chelovek.__momey)  #private нельзя выводить
# # chelovek.__money = 5
# # chelovek.__money = chelovek.__money + 5
# # print(chelovek.__money)
#
# chelovek._human_money += 5  # все таки можно (но осторожно)
#__________________________________________________________
#задача 1
# class Car:
#     def __init__(self):
#         self.status = False
#
#     def start(self):
#         if not self.status:
#             return "заведена"
#         else:
#             return "так она уже заведена"
#
#     def zapyck(self):
#         return "автомобиль заводится"
#
#     def otkl(self):
#         return "автомобиль глушется"
#
#     def y(self, year):
#         self.year = year
#
#     def t(self, type):
#         self.type = type
#
#     def c(self, color):
#         self.color = color
#
# avto = Car()
# avto.c("цвет борща")
# avto.y(2015)
# avto.t("обычный")
#
# print(avto.zapyck())
# print(avto.otkl())
#
# print("год:  ", avto.year)
# print("тип:  ", avto.type)
# print("цвет:  ", avto.color)
#
# avto.c("цвет борща")
# avto.y(2015)
# avto.t("обычный")
#__________________________________________________________
# import string
# class Alphabet:
#     def __init__(self):
#         self.__lang = "eng"
#         self.__letters = string.ascii_lowercase
#
#     def print(self):
#         return self.__letters
#
#     def letters_num(self):
#         return len(self.__letters)
#
#
# a = Alphabet()
# print(a.print())
#print(a.letters_num())
#__________________________________________________________
import datetime
class Overwatch:
    def __init__(self):
        self.__h, self.__m, self.__s = datetime.datetime.now().strftime("%H:%M:%S").split(":")
        self.__h, self.__m, self.__s = int(self.__h), int(self.__m), int(self.__s)

    def chas(self):
        self.__h += 1

    def vavod(self):
        return f"{str(self.__h).rjust(2,'0')}:{str(self.__m).rjust(2,'0')}:{str(self.__s).rjust(2,'0')}"

    def minuta(self):
        self.__m += 1

    def cecunda(self):
        self.__s

tome = Overwatch()
tome.chas()
print(tome.vavod())


