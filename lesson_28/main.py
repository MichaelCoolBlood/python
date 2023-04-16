from tkinter import *

def hell_o(evevet):
    messege = ent.get()
    ent.delete(0, END)
    print(messege)

root = Tk()  #создание/инициализация
root.geometry("500x400")
root.title("моё первое окошечко :3")
root["bg"] = "lightpink"

lab = Label(root, text="стендбуль")  #надпись
lab.pack()  #размещаем элемент(по порядку)

# lab["background"] = "pink"
# lab["foreground"] = "blue"
lab["bg"] = "pink"  #ключевым словом
lab["fg"] = "gold2"  #hex цвет
lab["font"] = ("arial", "20", "bold", "italic", "underline", "overstrike")  #1: размер шривта
lab["height"] = 3
lab["width"] = 15

btn = Button(root,
             text="моя первая кнопочка :з",
             bg="lightblue",
             font="20",
             #command=hell_o
             )
btn.pack()
btn.bind("<Double-Button-1>", hell_o)
# Button-1 = ЛКМ
# Button-3 = ПКМ

ent = Entry(root,
            width=10,
            bd=10)
#borderwidth
ent.pack()

txt = Text(root,
           width=20,
           height=5,
           wrap="none")
#wrap
#word - перенос по словам
#char - посимвольный
#none - без переноса
txt.pack()

root.mainloop()
#конец вселенной