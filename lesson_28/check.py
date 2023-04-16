#зыдычо1
# from tkinter import *
#
# okno = Tk()
# okno.geometry("200x400")
# texto = Label(okno, text="голибой")
# texto.pack()
# ent = Entry(okno,
#             width=32)
# ent.pack()
#
# btn1 = Button(okno,width=30,bg="red")
# btn1.pack()
# btn2 = Button(okno,width=30,bg="orange")
# btn2.pack()
# btn3 = Button(okno,width=30,bg="yellow")
# btn3.pack()
# btn4 = Button(okno,width=30,bg="green")
# btn4.pack()
# btn5 = Button(okno,width=30,bg="cyan")
# btn5.pack()
# btn6 = Button(okno,width=30,bg="blue")
# btn6.pack()
# btn7 = Button(okno,width=30,bg="purple")
# btn7.pack()
# okno.mainloop()
#__________________________________________________________
# from tkinter import *
# def mama():
#     messege = ent1.get()
#     ent1.delete(0, END)
#     messege1 = txt.get(0.0, END)
#     txt.delete(0.0, END)
#     print(messege, messege1)
#
# root = Tk()
# root.title("fffffffff")
# root.geometry("400x270")
# root["bg"]="#edd655"
#
# texto = Label(root, text="ваш адрес:", bg="white")
# texto.pack()
#
# ent1 = Entry(root, width=10)
# ent1.pack()
#
# texto2 = Label(root, text="коментарифагн:", fg="#edd655")
# texto2.pack()
#
# txt = Text(root, width=15, height=10)
# txt.pack()
#
# btn = Button(root, text="отправить", width=15, bg="#edd655", command=mama)
#root.mainloop()
#__________________________________________________________
from tkinter import *
def italian(one):
    lab['font'] = lab['font'].replace('italic', '')
    lab['font'] += ' italic'
def bold(two):
    lab['font'] =lab['font'].replace('bold', '')
    lab['font'] += ' bold'
def base(three):
    lab['font'] = lab['font'].replace('bold', '').replace('italic', '')



root = Tk()

lab = Label(root, text="привет")
lab["font"] = "arial 15 "
lab.pack()

lkm = lab.bind('<Button-1>', bold)
pkm = lab.bind('<Button-3>', italian)
lkm2 = lab.bind('<Double-Button-1>', base)


root.mainloop()





