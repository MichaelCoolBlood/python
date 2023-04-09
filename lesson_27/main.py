# c1 = input("Введите первый цвет: ").strip().lower()
# c2 = input("Введите второй цвет: ").strip().lower()
# c = ("красный", "жёлтый", "синий")
#
# if c1 not in c or c2 not in c:
#     print("Один из основных цветов введён неверно!")
# elif (c1 == c[0] and c2 == c[1]) or (c1 == c[1] and c2 == c[0]):
#     print("оранжевый")
# elif (c1 == c[1] and c2 == c[2]) or (c1 == c[2] and c2 == c[1]):
#     print("зелёный")
# elif (c1 == c[0] and c2 == c[2]) or (c1 == c[2] and c2 == c[0]):
#     print("фиолетовый")
# else:
#     print(c1.capitalize())
#__________________________________________________________
# n = input("начало первого урока: ")
# y = int(input("длинна урока: "))
# p = int(input("длинна перемен: "))
# ky = int(input("кол-во уроков: "))
# hours, minutes = n.split(":")
# hours, minutes = int(hours), int(minutes)
# t = hours*60 + minutes
# for i in range(ky):
#     print(f"{i+1} урок:", end="")
#     print(f"{str(hours).rjust(2,'0')}:{str(minutes).rjust(2,'0')} - ", end="")
#     t += y
#     hours = t // 60
#     minutes = t % 60
#     print(f"{str(hours).rjust(2,'0')}:{str(minutes).rjust(2,'0')}")
#__________________________________________________________




col_zomb = int(input("Сколько зомби было к началу расчёта: "))
vozm_zaraz = int(input("Сколько каждый может заразить: "))
day = int(input("На который день делаем расчёт: "))
print(f"1 день:{col_zomb}")

for i in range(2, day + 1):
    col_zomb = col_zomb = col_zomb * vozm_zaraz + col_zomb
    print(f"{i} день:{col_zomb}")



















