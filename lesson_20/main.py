# f = open("какойто дежурный в классе.txt","w", encoding="utf-8")  #создаст если нет, перезапишет если нет
# f.write("Heloow world\n")
# f.write("я играю в сабнавтику")
# f.close()
#__________________________________________________________
#f = open("какойто дежурный в классе.txt","r", encoding="utf-8")
#считываем содержимое файла и помещаем в content
# content = f.read()  #либо так
#__________________________________________________________
#задача
# name = input("название файла:  ")
# f = open(name + ".txt", "w", encoding="utf-8")
# msg = input("содержимое:  ")
# while msg != "":
#     f.write(msg + "\n")
#     msg = input("содержимое:  ")
#__________________________________________________________
#задача 2
# a = input("введите имя файла:  ")
# f = open(a, "r")
# content = f.readlines()
# print(content)
# v = len(content)
# for i in range(v):
#     print(f"{i+1})", content[i].strip())
#__________________________________________________________
#задача3
f = open("числа.txt", "r", encoding="utf-8")
text = f.readlines()
f.close()
print(text)
count = 0

while text != []:  #пока необработаны все линии
    elements = text[:3]
    count += 1
    f = open(str(count) + ".txt", "w", encoding="utf-8")
    for i in elements:  #элемент из троек
        f.write(i)
    del text[:3]




















