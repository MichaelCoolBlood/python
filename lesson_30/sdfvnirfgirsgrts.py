from tkinter import *
from random import randint
from tkinter import messagebox
root = Tk()
root.geometry("500x500")

# label1 = Label(root, text="логин:")
# label1.grid(column=0, row=0)
# label2 = Label(root, text="пароль:")
# label2.grid(column=0, row=1)
#
# entry1 = Entry(root,)
# entry1.grid(column=1, row=0)
# entry2 = Entry(root, show="*")
# entry2.grid(column=1, row=1)
#
# btn = Button(root, text="зачем она туть.,.,.,")
# btn.grid(column=1, row=3, sticky=E)
#__________________________________________________________

def fu(arms):
    btn.place(x=randint(0, 450), y=randint(0, 450))
def win():
    messagebox.showinfo(message="ты победил")

btn = Button(root, text="ПОИМАЁ МЕНЕ!", bg="red", command=win)
btn.place(x=10, y=10)
btn.bind("<Enter>", fu)








root.mainloop()