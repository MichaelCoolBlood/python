from pleer import MusicBox

pleer = MusicBox()
while True:
    pleer.play()
    guess = input("что ты услышал?")
    if guess == "":
        break
    pleer.check(guess)





































