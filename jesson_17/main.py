#попытка сделать игру кости
from random import randint
from time import sleep
print("игра кости, правила:\n "
      "вводишь количество бросков кубиков,\n"
      " после чего для первого и второго игрока\n"
      " бросается энное количество кубиков,\n"
      "числа выпавшие на кубиках складываются,\n"
      "у кого получилось больше баллов победил\n"
      "(может быть ничья)"
      "")

def roll_kub(bross):
    score = 0
    for i in range(bross):
        score += randint(1, 6)
    return score

bros = int(input("кол-во бросков: "))
score_ig1 = roll_kub(bros)
print("бросаем кости")
sleep(3)
print("баллы 1-го игрока:", score_ig1)
sleep(2)

score_ig2 = roll_kub(bros)
print("бросаем кости второго игрока")
sleep(3)
print("баллы 2-го игрока:",score_ig2)

print("анализ")
sleep(3)
if score_ig1 < score_ig2:
    print("второй игрок победил")
elif score_ig1 > score_ig2:
    print("первый игрок победил")
else:
    print("ничья")







