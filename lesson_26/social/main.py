from user import User

u1 = User(fam="смирнов", im="антон", log="smir-ant", pas="132456")
u2 = User()

# print(u1.login)
# print(u2.login)
#
# print(u1.familiya)
# print(u2.familiya)

users = [u1, u2]
l = input("введи логин: ")
p = input("введи пароль: ")
for chelovek in users:
    if chelovek.log_in(l, p):
        print("авторизация успешна")
        current = chelovek  #сохраняю текущего пользователя






