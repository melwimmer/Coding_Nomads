# Ask the player for their name.
# Display a message that greets them and introduces them to the game world.
# Present them with a choice between two doors.
# If they choose the left door, they'll see an empty room.
# If they choose the right door, then they encounter a dragon.
# In both cases, they have the option to return to the previous room or interact further.
# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.
# When encountering the dragon, they have the choice to fight it.
# If they have the sword from the other room, then they will be able to defeat it and win the game.
# If they don't have the sword, then they will be eaten by the dragon and lose the game.


Name = input("Good morning fellow crewmate, what is your name ").title()
print("Hello" + Name + "! you have reached the far far away land!")

chosendoor= None
sword = None
while True:
    chosendoor = input("You see two doors ahead of you! You have to chose left or right. 1").lower()
    if chosendoor == "right":
        desicionright = input("""Good job, you have reached the right room. 
        Oh ooooh! There's a dragon in this room, do you want to fight or exit the room? """ )
        if desicionright == "exit":
            continue
        if desicionright == "fight":
            if sword != True:
                exit = input(" You tried to fight the dragon without a weapon. That was brave, but unfortunately the dragon got the best of you. You died. Do you want to play again? Yes or No")
                if exit == "No":
                    break
                if exit == "Yes":
                    continue
            if sword == True:
                print("""You beat the dragon!! You are now safe. 
                You won!!!""")
                break
    if chosendoor == "left":
        desicionleft = input("You have choices to make. Do you want to look arround or exit the room? 1 ")
        if desicionleft == "look around":
            takesword = input("Looks like you found a sword! do you want to take it? Yes or No?")
            if takesword == "Yes":
                sword = True
            if takesword == "No":
                pass
            continue
        if desicionleft == "exit":
            continue

                
