import random
import datetime

while True:
    number = input("сколько дней рождения мы генерируем? (до 70)")
    if not number.isdigit() or int(number) > 70 or int(number) < 2:
        print("ВВЕДИ ПРАВИЛЬНО!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("=" * 10)
    else:
        number = int(number)
        break

birthdays = []
start_of_year = datetime.date(2022, 1, 1)

for _ in range (number):
    shift_of_days = datetime.timedelta(random.randint(0, 364))
    birthday = start_of_year + shift_of_days
    birthdays.append(birthday)

for index in range(number):
    print(f"{index + 1}) {birthdays[index]}")

print("=" * 10)
for i in set(birthdays):
    if birthdays.count(i) > 1:
        print(f"- {i.strftime('%d.%m.%y')} встречается {birthdays.count(i)} раза.")













