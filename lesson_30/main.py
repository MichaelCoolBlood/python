from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("500x500")

# lst = ["первый", "второй", "пятнадцать"]
# lstbox = Listbox(root)
# lstbox.pack()
# #первый способ через цикл и вставку
# for elem in lst:
#     lstbox.insert(END, elem)
#__________________________________________________________
#через переменную
# lst = ["первый", "второй", "пятнадцать"]
# lst_tk = StringVar(value=lst)  #получаем кортеж
# print(lst_tk.get())
# lstbox = Listbox(root, listvariable=lst_tk, selectmode=EXTENDED)
# lstbox.pack()
#
# def fu(pelmeni):
#     for ind in lstbox.curselection():  #current = текущий
#         print(lst[ind])
#
# lstbox.bind('<<ListboxSelect>>', fu)

# btn = Button(root, text="вывести", command=fu)
# btn.pack()
#__________________________________________________________
#messegebox
# messagebox.showinfo("туда_сюда", "ты проинформирован... теперь...")
# messagebox.showerror()
# messagebox.showwarning()
#__________________________________________________________
#pack.
#btn = Button(root, text="ткст")
#btn.pack(anchor=SW, expand=True)
#btn.pack(fill=BOTH, expand=True)
# btn1 = Button(root, text="ткст")
# btn1.pack(pady=50)
# btn2 = Button(root, text="ткст")
# btn2.pack(pady=50, ipadx=50)
#__________________________________________________________
#ряд - row
#столбик - column
# btn1 = Button(root, text="ткст1")
# btn1.grid(column=0, row=0)
# btn2 = Button(root, text="ткст2")
# btn2.grid(column=1, row=0)
# btn3 = Button(root, text="ткст3")
# btn3.grid(column=2, row=0, rowspan=2, sticky=NS)
# btn4 = Button(root, text="ткст4")
# btn4.grid(column=0, row=1, columnspan=2, sticky=EW)
# _________________________________________________________
# btn1 = Button(root, text="ткст1")
# btn1.place(x=10, y=10)
#__________________________________________________________
from time import sleep
# def fu():
#     print("print")
#     root.after(1000, fu)
#
# root.after(3000, fu)
#__________________________________________________________
# def fu(pelmeni):
#     print("print")
#
# btn1 = Button(root, text="ткст1")
# btn1.pack()
#btn1.bind("<Enter>", fu) #принаведении мышкой
#btn1.bind("<MouseWheel>", fu)  #кручение колеса мыши
#btn1.bind("<FocusIn>", fu)  #фокус (tab)
# btn1.focus_set()
# btn1.bind("<Return>", fu)
# btn1.bind("<h>", fu)#h
# btn1.bind("<Shift-Up>", fu)
#__________________________________________________________
# rb_val = IntVar()
# print(rb_val.get())
# rb_val.set(5)
# print(rb_val.get())
# _________________________________________________________
# Entry(root, show="*").pack()
#__________________________________________________________

root.mainloop()