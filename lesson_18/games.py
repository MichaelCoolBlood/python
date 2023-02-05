import easygui
import random

def rock_paper_scissors():
    b="img/б.png"
    k="img/к.png"
    n="img/н.png"
    user=easygui.buttonbox(
        images=[b, k, n],
        choices=("выйти",),
    )

    comp=random.choice([b,k,n])

    if user == b and comp == b:easygui.msgbox(msg="ничья")

    elif user == b and comp == k:easygui.msgbox(msg="выйгрол")
    elif user == b and comp == n:easygui.msgbox(msg="проигролл")
    elif user == k and comp == n:easygui.msgbox(msg="выйгрол")
    elif user == k and comp == k:easygui.msgbox(msg="ничья")
    elif user == k and comp == b:easygui.msgbox(msg="проигролл")
    elif user == n and comp == n:easygui.msgbox(msg="ничья")
    elif user == n and comp == b:easygui.msgbox(msg="выйгралл")
    else:easygui.msgbox(msg="проигролл")

    print(user, comp)


def guess_the_number():
    chislo = random.randint(1, 100)
    gn = easygui.integerbox(upperbound=100, lowerbound=1, msg="попробуй угадать число от 1 до 100")
    while gn != chislo:
        print(gn, chislo)
        if gn > chislo:
            gn=easygui.integerbox(upperbound=100, lowerbound=1, msg=f"нет, нужно число меньше чем {gn}", image="img/меньше.png")
        elif gn < chislo:
            gn=easygui.integerbox(upperbound=100, lowerbound=1, msg=f"нет, нужно число больше чем {gn}", image="img/больше.png")

    easygui.msgbox(msg="побеедаа")







games = [
    'Камень, ножницы, бумага',
    'Угадай число'
]

games_entry_points = [
    rock_paper_scissors,
    guess_the_number
]

while True:
    res = easygui.buttonbox('Выбери игру!', choices=games)
    if res is None:
        break
    games_entry_points[games.index(res)]()


































