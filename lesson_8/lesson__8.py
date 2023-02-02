# import random
# print(random.randint(0, 100))
#
# import random as r
# print(r.randint(0, 100))
#
# from random import randint
# print(randint(0, 100))
#
# from random import *
# print(randint(0, 100))
#
# import random as r
# lst = [0, 1, 2, 3, 4, 5]
# print(r.choice(lst))
# r.shuffle(lst)
# print(lst)
#__________________________________________-


import turtle
screen = turtle.Screen()
t = turtle.Turtle()

# t.forward(250)
# t.back(100)
horizontal = 200
vertical = 100

t.pensize(5)

t.color("red", "yellow")

t.speed(2)

t.begin_fill()

t.shape("turtle")

t.fd(horizontal)
t.right(90)
t.fd(vertical)
t.rt(90)
t.fd(horizontal)
t.rt(90)
t.fd(vertical)
t.rt(90)
t.end_fill()


t.penup()
t.goto(120, -40)
t.pendown()
t.fd(50)

t.circle(30)
t.circle(40)

t.write("momamvi", font =("Arial Black", 25, "normal"), align = "center")






screen.exitonclick()




