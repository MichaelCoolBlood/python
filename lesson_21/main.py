f = open("file.txt", "w", encoding="utf-8")
# f.write("А, э")
# f.close
#__________________________________________________________
# try:
#     f = open("filegh.txt", "r", encoding="utf-8")
# except FileNotFoundError:
#     print("ы")
#__________________________________________________________

# try:
#     x = int(input("введи число:  "))
#     print(10 / x)
# except ValueError:
#     print("хотелось бы число")
# except ZeroDivisionError:
#     print("да ну нэ")
# else:
#     print("*гордый Ы*")
# finally:
#     print("")
# __________________________________________________________
# x = input("введи имя друга:")
# try:
#     if x == "Антон":
#         raise NameError("ахаха")
# except NameError as pelmeni:
#     print("не льзя", pelmeni)
#__________________________________________________________
# def sr_ar():
#     s = 0
#     k = 0
#     for number in text:
#         try:
#             s += int(number)
#         except ValueError:
#             print("найдено не число:", number)
#         else:
#             k += 1
#     # print(s)
#     # print(k)
#     if k == 0:
#         print("числа отсутствуют")
#     return  round(s/k, 2)
#
# try:
#     f = open("file.txt", "r", encoding="utf-8")
# except FileNotFoundError:
#     print("файл отсутстует или неправильное название")
# text = f.read().split()
# f.close()
#
# print(sr_ar())
# #__________________________________________________________
# try:
#     f = open("file.txt", "r", encoding="utf-8")
# except FileNotFoundError:
#     print("файл отсутстует или неправильное название")
# text = f.readlines()
# print(f"строк: {len(text)}")
#
# full_text = " ".join(text).replace("\n", " ")
# #print(full_text)
# words = full_text.split()
# print(f"слов: {len(words)}")
# symbols = full_text.replace(" ", "")
#
# print(f"символов: {len(symbols)}")

# f.close()
#print(text)
#__________________________________________________________
# word = input("какое слово ищем:  ")
# try:
#     f = open("filex.txt", "r", encoding="utf-8")
# except FileNotFoundError:
#     print("файл отсутстует или неправильное название")
# text = f.read()
# f.close()
#
# print(text.count(word))
#__________________________________________________________
try:
    f = open("file.txt", "r", encoding="utf-8")
except FileNotFoundError:
    print("файл отсутстует или неправильное название")
text = f.read()
f.close()

numbers = text.split()
print(numbers)
p = 1
for i in numbers:
    p *= int(i)
print(p)





