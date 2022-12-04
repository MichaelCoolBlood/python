# a = int(input("a: "))
# b = int(input("b: "))
# lst = []
#
# for aaa in range(a + 1, b):
#     lst.append(aaa ** 2)
# print(lst)

# x = input("ввод: ")
# lst = x.split(" ")
# print(lst)
# lst.reverse()
# print(lst)

# number = input("число: ")
# chet = 0
# nechet = 0
# lst = []
# 
# while number != "end":
#     number = input("число: ")
#     if number.lstrip("-").isdigit():
#         number = int(number)
#         lst.append(number)
#     elif number == "end":
#         break
#     else:
#         print("число пожадуста")
#         continue
# 
#     if number % 2 == 0:
#         chet += 1
#     else:
#         nechet += 1
# 
# print(lst)
# print(f"четные: {chet}шт.")
# print(f"нечетные: {nechet}шт.")

lst = [-5, -8, 2, 14, 1]
mini = min(lst)
maxi = max(lst)

lst[lst.index(mini)]
lst[lst.index(maxi)]

lst[lst.index(mini)], lst[lst.index(maxi)] = lst[lst.index(maxi)], lst[lst.index(mini)]
print(lst)











