import random

life = 10
length = 3

answer = random.randint(100, 999)
answer = str(answer)  # число -> строчку

while life:  # то же самое, что и while life != 0
    is_guessed = False  # отгадано?
    print("=" * 10)

    #print("Жизней:", life)
    print("жизней:", end="")
    for _ in range(life):
        print("❤", end="")
    print()

    guess = input("Предположение: ")
    if len(guess) != length or not guess.isdigit():  # если длина != 3 или не число
        print("Число от 100 до 999, пожалуйста!")
        continue

        #проверка правельного ответа
    if guess == answer:
        print("победа")
        is_guessed = True
        break

    if is_guessed == False:
        for i in range(length):  #от нуля до двух
            if guess[i] == answer[i]:
                print("Fermi ура")
                is_guessed = True
                break #выход из for

    if is_guessed == False:
        # проверка на пико

        for char in guess:
            if char in answer:  #есть ли такое число в ответе
                print("Pico 😀 ")
                break  #выход из for

    if is_guessed == False:
        print("bagels 😔")

    life -= 1

























