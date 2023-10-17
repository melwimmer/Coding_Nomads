import random


guess= None
guess_response = False

number= random.randint(1,10)
counter = 0 


while counter < 3:
    counter += 1
    while guess != number: 
        guessed_number = input("Guess a number between 1 and 10")
        guess = int(guessed_number)
        if guess != number:
            print("Not correct, try again")
            break
        
    else:
        print("You got it!")
else:
    print("ran out of tries")




 
