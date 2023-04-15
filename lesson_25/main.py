# class Class:
#     city = "новосибирск"  #public static
#     def __init__(self, x=35):
#         self.x = x  #public dynamic
#         self.location = Class.city
#
# obj = Class(350)
# print(obj.x)
#__________________________________________________________
from _random import randint
class Human:
    default_name = "Никита"
    default_age = 42
    def __init__(self, name=default_name, age=defalt_age):
        self.name = name
        self.age = age
        self.__money = 1_000
        self.__house = None
    def info(self):
        return (self.name, self.age, self.money, self.__house)
    def earn_money(self):
        self.__money += 5
    def defalt_info(self):
        return (Human.defalt_name, Human.default_age)
    def __make_deal(self):
        if self.__money >= dom.final_price():
            self.__money -= dom.final_price()
            return True
    def buy_house(self, dom):
        if self.__make_deal():
            print("ура")
        else:
            return f"денег не хватает, тебе не хватает: {self.__money -= dom.final_price()}"


class House:
    def __init__(self, ar:str, pr:int):
        self.__area = ar
        self.__price = pr
        self.__skidka = randint(5, 25)  #в %
    def final_price(self):
        return self.__price - (self.__price * (self.__skidka / 100))





artem = Human(age=0, name="Гриша")
dom1 = House("Новосибирск", 1300)
print(artem.buy_house(dom1))
artem.buy_house(dom1)

















