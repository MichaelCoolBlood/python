import random
import art

print(art.intro)

vocabulary = ['Anton', 'Alex', 'Alexandr', 'Arsalan', 'Danil', 'Kirill', 'Sergey', 'Nikolay', 'Nasty', 'Natasha', 'Ivan', 'Igor', 'Gosha', 'Galina', 'Olya', 'Oksana', 'Oleg', 'James', 'Bill']

word_answer = random.choice(vocabulary).lower()
word_display = []

print(vocabulary[:len(word_answer)])
print(vocabulary[len(word_answer):])  #запара чтобы имена вместились

for _ in range(len(word_answer)):
    word_display.append("_")

print(word_display)
life = 6
counter = 0

while life > 0 and counter != len(word_answer):
    print(art.stages[life])
    letter = input(("буква:  "))
    letter_is_be = False
    for i in range(len(word_answer)):
        if letter == word_answer[i]:
            if word_display[i] != "_":
                letter_is_be = True
            else:
                word_display[i] = letter
                letter_is_be = True
                counter += 1

    if letter_is_be == False:
        life -= 1
    print(word_display)
if counter == len(word_answer):
    print("не сейчас так в следующий")
else:
    print(art.stages[life])
    print("проиграл")




























