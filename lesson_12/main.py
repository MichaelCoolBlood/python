#мутабельность
#мутабельные - изменяемые
#немутабельнные - неизменяевые
# x = "movavi"
# x[i] = "o" #так низя
# x = "movovi"

# списки []
# lst = ["один","два","три",]
# lst.append("спинер")  #.append() - добавить
# lst.pop(0)  #.pop - удалить по индексу
# lst.remove("два") #.remove - удалить по значению

# lst = [0, 1, 2, 3]
# lst.reverse() # .reverse - перевернуть
# print(lst)

# lst1 = [0, 1, 2]
# lst2 = [3, 4, 5]
# lst1.extend(lst2) # .extend - разширить
# print(lst1)

# lst = [1, 2]  #
# lst.insert(1, 1.5) #.insert - вставить

# lst = ["не пустота"]
# lst.clear() #.clear - очистка

# lst = [0, 1, 2, 3, 4]
# lst.sort() #.sort - сортировка
# lst.sort(reverse=True) #.sort(reverse=True) - от меньшего к большему
# print(lst)
#__________________________________________________________________
#кортеж
# tup = (1, 2, 3)
# # tup = 1, 2, 3
# # tup = 1,
# print(max(tup))
# print(min(tup))
#__________________________________________________________________
# list1 = ["A", "B", "C",]
# list2 = ["1", "2", "3",]
# couple = zip(list1, list2) # zip - функция обьединения по индексу
#
# for bogdan in couple:
#     print(bogdan)
#___________________________________________________________________
from collections import namedtuple

citizen = namedtuple("житель", "имя, возраст, статус")
alex = citizen(имя="Лёха Алексеев",
               возраст="27",
               статус="предприниматель")

print(alex.имя)
print(alex.статус)

print(alex)






