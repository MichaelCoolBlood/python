# a = int(input("а:  "))
# print(a + 2 - (a % 2))
# -----------------------------------------------------------
#задача 1
# a = input("строка:  ")
# if len(a) > 5:
#     print(a[:3], a[-3:])
# else:
#     print(a[0] * len(a))
# -----------------------------------------------------------
#list comprehension
#[1, 2, 3, 19, 40]
# answer2 = [chislo ** 2 for chislo in range(1, 6) if chislo ** 2 % 2 == 0]
# print(answer2)
# -----------------------------------------------------------
# bukvi  = "abcdef"
# print("Цибин".join(i.upper()*2 for i in bukvi))
#
# -----------------------------------------------------------
#задача 2
# a = input("строка:  ")
# answer = []
# for element in a:
#     if element.isdigit():
#         answer.append(int(element))
# print(answer)
# -----------------------------------------------------------
# a = input("строка:  ")
# print([int(i) for i in a if i.isdigit()])
# -----------------------------------------------------------
#задача 3
# a = int(input("расчисол:  "))
# print(format(a, ","))
# -----------------------------------------------------------
# a = [-1, 2, 3, -2, 5]
# print([elem for elem in a if elem >= 0])
# -----------------------------------------------------------
# a = [5, 7, 4, 3, 4]
# l = []
# for indx in range(len(a) - 1):
#     if a[indx] < a[indx+1]:
#         l.append(a[indx+1])
# print(l)
# ___________________________________________________________
# a = [3, 18, 4, 5, 1, 3]
# ans = []
# for i in range(2):
#     maxi = max(a)
#     ans.append(maxi)
#     a.remove(maxi)
# print(ans)
# ___________________________________________________________
# a = [3, 18, 4, 5, 1, 3]
# print(sorted(a)[-2:][::-1])
# ___________________________________________________________
# a = input("а:  ")
# print(a == a[::-1])
# ___________________________________________________________
# a = [1, 2, 3, 4, 5]
# indx1 = a.index(max(a))
# indx2 = a.index(min(a))
# a[indx1], a[indx2] = a[indx2], a[indx1]
# print(a)
# ___________________________________________________________
import random
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(5):
    print(a.pop(random.randint(0, len(a) - 1)))
print(a)



