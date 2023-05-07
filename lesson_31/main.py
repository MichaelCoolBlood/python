from tkinter import *
root = Tk()
root.geometry('550x550')

c = Canvas(root, height=500, width=500, bg="wheat")
c.pack(anchor=CENTER, expand=True)
# TEXT
# c.create_text(10, 10,
#               text="чпп-мнн",
#               anchor=NW,
#               font="Arial 25 bold",
#               fill='magenta')
# RECTANGLE
# c.create_rectangle(10, 10,
#                    150, 100,
#                    fill='brown',
#                    outline='blue',
#                    width=10)
# POLYGON
# c.create_polygon(10, 10,
#                  150, 150,
#                  10, 150)
# OVAL
# c.create_oval(10, 10,
#               150, 250,)
# ARC
# c.create_arc(10, 10,
#              150, 150,
#              extent=45,
#              start=45)
# хорда
# c.create_arc(10, 10,
#              150, 150,
#              extent=300,
#              start=45,
#              style=CHORD)
#дуга
# c.create_arc(10, 10,
#              150, 150,
#              extent=30,
#              start=45,
#              style=ARC,
#              outline="purple",
#              width=5)
# отрисовка
# c.create_rectangle(10, 10,
#                    150, 100,
#                    fill="brown",
#                    outline='blue',
#                    width=10,
#                    dash="-",
#                    activefill="pink",
#                    activewidth=15)
#event
def chupapi(event):
    print(event.x, event.y)

btn = Button(root, text="кнопка")
btn.pack()
btn.bind("<Button-3>", chupapi)
































































































































root.mainloop()






























