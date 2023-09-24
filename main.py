# def abc(a: int = 5) -> str:   #type hint
#     return a
# func = lambda a, b: a + b
# print(func(2,3))
# ___________________________________________________________
#классы. полиморфизм. наследование. инкапсуляция.
# class human:
#     pi = 3.14   #статический атрибут
#     def say(self, fraza):   #публичный метод
#         return fraza
#
#     def __init__(self, vozrast: int = 0):   #initialization
#         print("я создался")
#         self.age = vozrast   #динамический атрибут
#         self.money = 0
#
#     def __sad(self):   #приватный метод
#         print("😑😐😶")
#
#     def work(self):
#         self.money += 1000
#         self.__sad()   #можно использовать только внутри класса
#
#     def __call__(self, *args, **kwargs):
#         print(f"я человек, мне {self.age} лет и я имею {self.money} руб")
#
#     def __add__(self, other):
#         if type(other) == int:
#             return "мандарика " * other
#         return "мандаринка"
#
# grisha = human(12)   #создание обьекта на основе класса -> init
# print(grisha.say("привет"))
# print(grisha.age)
# grisha.age = 50   #меняем атрибут
# anton = human(21)
# anton = human()
# print(anton.say("На урок!"))
# anton.work()
# print(anton.money)
# grisha()
# print(anton + 0)   #мандаринка * 0
# print(anton + 2)   #мандаринка * 2
# print(anton + 0.0)   #мандаринка * 0
# ___________________________________________________________
class Adc:
    def __init__(self):
        self.parampampam = 5

    def komanda(self):
        return "Я - команда"

class Def(Adc):   #наследование (abc - родительский класс
    def action(self):
        return "Я - шон"

a = Adc()
print(a.parampampam)
b = Def()
print(b.parampampam)
print(a.komanda())


# print = input()
# print(6)

























