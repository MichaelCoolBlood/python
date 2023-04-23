from tkinter import *
win = Tk()
win.geometry("400x200")
win['bg'] = "pink"

#надпись
# lab = Label(win, text="чбтыолбоы")
# lab.pack()
# lab['bg'] = "lightblue"
# lab['foreground'] = "#65d5f6"

#однострочный ввод
# ent = Entry(win,
#             width=8,
#             borderwidth=10,
#             font="arial 500")
# ent.pack()

#многострочный ввод
# txt = Text(win, width=20, height=3, wrap='word')
# txt.pack()

#фнопка
# def action()
#     print("пруинт")
# btn = Button(win, command=action)
# btn['text'] = "я фнопка"
# btn.pack()

#check button
# def get_cb():
#     print(cb_val.get())
#
# cb_val = BooleanVar()
# cb = Checkbutton(win,
#                  text="jfbjfgbugfhfghuf",
#                  command=get_cb,
#                  variable=cb_val,
#                  onvalue=True,
#                  offvalue=False)
# cb.pack()
# cb.select()
# cb.deselect()

#radiobutton
# def get_rb():
#     (rb1_val.get())
#
# rb1_val = IntVar()
# rb1 = Radiobutton(win,
#                  text="туксто",
#                  variable=rb1_val,
#                  value=1,
#                  command=get_rb)
# rb1.pack()
# rb2_val = IntVar()
# rb2 = Radiobutton(win,
#                  text="туксто",
#                  variable=rb2_val,
#                  value=2,
#                  command=get_rb)
# rb2.pack()

#scale
# def get_scala(val):
#     print(scala.get())
#
# scala = Scale(win,
#               from_=50,
#               to=120,
#               orient=HORIZONTAL,
#               length=300,
#               tickinterval=10,
#               resolution=10,
#               command=get_scala)
# scala.pack()

#фотокарточка
# img = PhotoImage(file="истинная грань ночи.png")
# img_small = img.subsample(1,10)
# img.big = img.zoom(3,3)
# img_poltora = img.subsample(3,3).zoom(2,2)
# lab = Label(win, image=img_poltora)
# lab.pack()

#отступы
# Label(win, text="кис-кис", bg="gold").pack()
# Label(win, text="xис-xис", bg="lightblue").pack()











win.mainloop()








