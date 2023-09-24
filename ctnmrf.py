class User:
    def __init__(self, imya, parol, login):
        self.name = imya
        self.password = parol
        self.nickname = login
        self.followers = []   #тот кто подписан на тебя
        self.subscrabers = []   #тот на кого подписан ты
        self.session = False

    def change_pas(self):
        if input("введи старый пароль:  ") == self.password:
            self.passowrd = input("введите новый пароль:  ")
            print("аля новый пароль установлен ✔")
        else:
            print("отказано")

    def authorize(self):
        while True:
            if not self.session:  #если не вошёл
                if input("логин: ") == self.nickname and \
                    input("пароль:  ") == self.password:
                    self.session = True
                else:
                    print("ты не вошёл, попробуй ещё раз")
            else:   #вошёл = сидишь в акаунте
                print("\n" * 50)
                input("что будем делать?")


u1 = User("верочк", "123", "vryia1.5")
u2 = User("бандик", "slomo", "ban000")
#u1.change_pas()
u1.authorize()











