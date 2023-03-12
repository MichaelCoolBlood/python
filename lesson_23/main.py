import json
# f = open("file.json", "w", encoding="utf-8")
# json.dump("прифки", f, ensure_ascii=False)
# f.close()
#__________________________________________________________
# f = open("file.json", "r", encoding="utf-8")
# c = json.load(f)
# f.close()
# print(c)
#__________________________________________________________
# class person:
#     def __init__(self, imya, vozrast):  #магический метод инициализаии
#         self.name = imya
#         self.age = vozrast
#     def __str__(self):
#         return f"я {self.name} и мне {self.age} лет"
#
#
# chelovek = person("донис", 29)  #создание обьекта класса person
# chelovek2 = person("витол", 5)
#
# print(chelovek.name)
# print(chelovek2.name)
#
# print(chelovek)
# print(chelovek2)
#__________________________________________________________
# class Klass:
#     def __init__(self ,imya, familia, age):
#         self.name = imya
#         self.familia = familia
#         self.voz = age
#
#     def __str__(self):
#         return f"возраст: {self.voz}\nимя: {self.name}\nфамилия: {self.familia}"
#
#     def greet(self):
#         return f"привет меня зовут: {self.name}, мне: {self.voz} лет"
#
# man = Klass("тимейт", "sss", 12)
# #print(man.name, man.familia, man.voz)
# #print(man)
# print(man.greet())
#__________________________________________________________
import random
# list = []
# for i in range(random.randint(5, 10)):
#     list.append(random.randint(2, 5))
# print(list)
# nums = [random.randint(2, 5) for _ in range(random.randint(5, 10))]
# print(nums)
class person:
    def __init__(self ,imya, familia, age):
        self.name = imya
        self.familia = familia
        self.voz = age
        self.grades = [random.randint(2, 5) for _ in range(random.randint(5, 10))]
        self.srbal = sum(self.grades)/len(self.grades)

    def __str__(self):
        return f"возраст: {self.voz}\nимя: {self.name}\nфамилия: {self.familia}"

    def greet(self):
        return f"привет меня зовут: {self.name}, мне: {self.voz} лет"

man = person("тимейт", "sss", 12)
manx = person("тим", "s", 1)
#print(man.name, man.familia, man.voz)
#print(man)
print(man.grades, man.srbal)













































































































































