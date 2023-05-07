from tkinter import *
# root = Tk()
# root.geometry("450x450")
# img = PhotoImage(file='кртнк.png').subsample(2, 2)
# c= Canvas(root, height=450, width=450, bg="white")
# c.pack(anchor=CENTER)
# second = 0
#
# def seconds():
#     global second
#     c.delete("all")
#     second += 1
#     c.create_image(225, 215, image=img)
#     c.create_text(int(c["height"]) / 2, 450 / 2, text=second, font="Arial 50")
#     root.after(1, seconds)
#     if second == 15:
#         root.destroy()
#
# c.create_text(int(c["height"])/2, 450/2, text=second ,font="Arial 50")
# c.create_image(225, 215, image=img)
# root.after(1000, seconds)
#__________________________________________________________
root = Tk()
root.geometry("500x500")

c = Canvas(root, height=400, width=400, bg="white")
c.pack()

l = None
p = None

def lkm(event):
  global  l
  l = (event.x, event.y)
  print(l)
def pkm(event):
  global p
  p = (event.x, event.y)
  print(p)

def strotel():
  c.create_line(l[0], l[1], p[0], p[1])

btn = Button(root, text="Построить прямую", command=strotel)
btn.pack()
c.bind("<Button-1>", lkm)
c.bind("<Button-3>", pkm)







































root.mainloop()