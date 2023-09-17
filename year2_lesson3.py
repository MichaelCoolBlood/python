# def nazvanie(name: str = "terratech world") -> str:  #type hint
#     """ghghghhghghghghgghghhg"""
#     return name
# print(nazvanie("нейм"))
# ___________________________________________________________
# def funkcia(namee: list):
#     return sum(namee)
# print(funkcia([52, 2, 3, 0, -1]))
# ___________________________________________________________
# def funcia(nameee: list) -> tuple:
#     return tuple(max(nameee), min(nameee))
#     print(funcia([52, 2, 3, 0, -1]))
# ___________________________________________________________
# def funciae(nameeee: list) -> list:
#     for i in nameeee:
#         if nameeee.count(i) > 1:
#             nameeee.remove(i)
#     return sorted(nameeee)
# print(funciae([1, 0, 2, 1]))
# ___________________________________________________________
# def fuca(nameeeee: list) -> dict:
#     d = {'int' : 0,
#          'str' : 0,
#          'float' : 0,
#          'bool' : 0}
#     for i in nameeeee:
#         if type(i) == int:
#             d['int'] += 1
#         elif type(i) == str:
#             d['str'] += 1
#         elif type(i) == str:
#             d['float'] += 1
#         else:
#             d['bool'] += 1
#         return d
# print(fuca([1, 'два', True, 3.14, "четыре", False]))
# ___________________________________________________________
# def fuccccia(nameeeeee: int) -> list:
#     chtoto = [0, 1]
#     while chtoto[-1] <= nameeeeee:
#         chtoto.append(chtoto[-1]+chtoto[-2])
#     return chtoto[:-1]
# print(fuccccia(355))
# ___________________________________________________________
# def fuciia(nameeeeeee: list, nnameeeeeee:list):
#     return sorted(nameeeeeee+nnameeeeeee)
# print(fuciia([1, 5, 8, 11] [2, 5]))
# ___________________________________________________________
# d = {
#     "add": lambda x: c + x,
#     "minus": lambda x: c - x,
#     "div": lambda x: c // x,
#     "mul": lambda x: c * x,
# }
#
# # def add(x:int) -> int:
# #     return c + x
# c = 0
# while True:
#     zapros = input().split()
#     if len(zapros) == 1:
#         zapros = zapros[0]
#         if zapros == "exit":
#             break
#         elif zapros == "result":
#             print(c)
#         elif zapros == "zero":
#             c = 0
#     else:   # math oper
#         c = d[zapros[0]](int(zapros[1]))
#         # if zapros[0] == "add":
#         #     c = add(int(zapros[1]))
# ___________________________________________________________
def is_sorted(l:list) -> bool:
    return l == sorted(l)

print(is_sorted([3, 7, 1]))
print(is_sorted(sorted([3, 7, 10])))




