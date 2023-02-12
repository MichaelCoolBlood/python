alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_ru = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
alphabet_ru_x = alphabet_ru[::-1]
alphabet_x = alphabet[::-1]

ti = input("введи сообшение, я переведу его шифр атбаша:  ")
phrase2 = ''
for i in ti:
    if i.upper() in alphabet_ru:
        ind = alphabet_ru.index(i)
        bukva = alphabet_ru_x[ind]
        phrase2 += bukva
    elif i not in alphabet or alphabet_ru:
        phrase2 += i
    elif i.upper() in alphabet:
        ind = alphabet.index(i)
        bukva = alphabet_x[ind]
        phrase2 += bukva
print(phrase2)
# ___________________________________________________________






























