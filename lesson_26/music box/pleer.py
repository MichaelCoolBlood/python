from random import choice
import playsound

class MusicBox:
    def __init__(self):
        self.__variants = "eiqz"
        self.__score = 0
        self.__sequense = choice(self.__variants)

    def get_score(self):
        return self.__score

    def play(self):
        for bukva in self.__sequense:
            playsound.playsound(f"sounds/{bukva}.mp3")

    def check(self, predpologenie):
        if predpologenie.lower() == self.__sequense:
            playsound.playsound("sounds/correct.wav")
            self.__score += 1
            self.__next()
        else:
            playsound.playsound("sounds/incorrect.wav")
            self.__score -= 0.5

    def __next(self):
        __dlina = len(self.__sequense) + 1
        self.__sequense = ""
        for _ in range(__dlina):
            self.__sequense += choice(self.__variants)










