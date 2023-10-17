import random
num = random.randint(1,10)

guessed_number = None

while num != guessed_number:
    guessed_number = int(input("Guess a number from 1-10 "))
    if guessed_number == num:
        print("We did it we did it we did it siii!!")
        break
    else:
        print("Sorry, try again!")