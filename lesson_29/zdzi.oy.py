from tkinter import  *

# def knopka(event):
#     messege = ent.get()
#     lab["text"] = messege
#
# root = Tk()
# root.geometry("400x200")
#
# lab = Label(root, text="у.у.у.у.у..у.у.у.у..у.у.у..у.у.у.у")
# lab.pack()
#
# ent = Entry(root)
# ent.bind("<Button-3>", knopka)
# ent.insert(0, "впиши и пкм ПпП")
# ent.pack()
#root.mainloop()
#__________________________________________________________
# def hel_lo(event):
#     user_choose = rb_val.get()
#     if user_choose == 1:
#         lab["text"] = "Heloo"+ rb1["text"]
#     else:
#         lab["text"] = "Heloo"+ rb2["text"]
#
#
# root = Tk()
#
# lab = Label(root, text="Hello")
# lab.pack()
#
# rb_val = IntVar()
#
# rb1 = Radiobutton(root, text="World", variable=rb_val, value=1, command=hel_lo)
# rb1.pack()
#
# rb2 = Radiobutton(root, text="Pyton", variable=rb_val, value=2, command=hel_lo)
# rb2.pack()
#
# root.mainloop()
#__________________________________________________________
from tkinter import *
def activator():
    if cb_val.get() == True:
        b["text"] = "активна"
        b["state"] = "normal"
    else:
        b["text"] = "не активна"
        b["state"] = "disabled"

win = Tk()
cb_val = BooleanVar()
cb = Checkbutton(win, text="акутивотар виндовс", variable=cb_val, onvalue=True,
                 offvalue=False, command=activator)
cb.pack()
b = Button(win, text="не активна", state="disabled")
b.pack()











win.mainloop()