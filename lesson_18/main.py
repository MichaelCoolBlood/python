import easygui
#
# user_choose = easygui.msgbox(
#     msg="Hello world",
#     title="усилено приветствую",
#     ok_button="понятно",
#     image="img/tank.png"
# )
#
# if user_choose == None:
#     easygui.msgbox(msg ="ну пока")
# elif user_choose == "понято":
#     print("ы")
#__________________________________________________________

# easygui.buttonbox(
#     msg="какой ты сегодня",
#     title="заголовок",
#     choices=("загадочный",),
#     images=["img/указатель.png", "img/tank.png"]
# )
#__________________________________________________________
# x = easygui.integerbox(
#     msg="число от 50 до 150",
#     upperbound=150,
#     lowerbound=50,
#     image="img/указатель.png"
#     defant=-632
# )
# print(x)
#__________________________________________________________
name = easygui.enterbox(
    msg="какое погоняло собаки(друга)",
    default="женя предатель"
)
print(name)

















