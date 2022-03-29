from operator import truediv
import random

win = False
replay = True

while replay == True:
    win = False
    limit = input("Bitte gebe deine Höchstzahl ein:\n")
    limit = int(limit)
    randint = random.randint(0, limit)
    print(randint)
    print("Ich habe meine Zahl, fang an zu raten!")

    while win == False:
        guess = input()
        guess = int(guess)
        if guess < randint:
            print("Die Zahl ist größer.")
        elif guess > randint:
            print("Die Zahl ist kleiner.")
        elif guess == randint:
            win = True
            print("Ja, da ist meine Zahl!")
            break

    nochmal = input("Willst du nochmal spielen?\n(1) Ja\n(2) Nein")
    nochmal = int(nochmal)
    if nochmal - 1 == 1:
        replay = False
