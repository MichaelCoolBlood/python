import os

total_bets = []
triger = "yes"

while triger == "yes":
    name = input("имя: ")
    bet = int(input("ставка: "))
    temp_bet = {"name": name, "bet": bet}
    total_bets.append(temp_bet)
    triger = input(("yes - продолжаем, no  - останавливаем: "))
    os.system("cls")

whinner = {'name': '', "bet": 0}
for i in range(len(total_bets)):
    if total_bets[i]["bet"] > whinner['bet']:
        whinner["name"] = total_bets[i]['name']
        whinner["bet"] = total_bets[i]['bet']
print(f"победитель: {whinner['name']}. его ставка: {whinner['bet']}")



























