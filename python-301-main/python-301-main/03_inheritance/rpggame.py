#
import random

class Character():
     def __init__(self, strength, max_strength):
        self.max_strength = max_strength
        self.strength = strength

class Hero(Character):
     def boostxp(self):
         self.strength +=10
         print(f'You now have {self.strength} XP')

class BossOponent(Character):
     def fight(self, other):
        rand_fight = random.choice(["boss", "me"])
        if rand_fight == "me":
            other.strength -= 0.1*other.strength
            print(f'You won! Your XP is {self.strength} and the dragons XP is {other.strength}')
        else:
            self.strength -=0.1*self.strength
            print(f'You lost.. Your XP is {self.strength} and the dragons XP is {other.strength}')  

        if other.strength == 0:
            self.max_strength = (other.max_strength*1.5) + self.max_strength
            self.strength = self.max_strength
            print(f'You have leveled up. Your max strength is {self.max_strength} and you recovered your health')    

me = Hero(30, 30)
dragon = BossOponent(200,200)
chicken = BossOponent(1,1)
trashpanda = BossOponent (20,20)




print("whoops, you found a dragon!")
while True:
    while me.strength != 0 and dragon.strength !=0:
        forb = input(f'do you want to fight the dragon? Or do you want to boost your XP? You have {me.strength} of strength left. Choose fight or boost')
        if forb == 'fight':
            me.fight(dragon)
        elif forb == 'boost':
            me.boostxp()
        else:
            continue
    else:
        if me.strength == 0:
            print('You lost')
            break
            
        else:
            print("You Won!")
            break
            

    












# Name = input("Good morning fellow crewmate, what is your name ").title()
# print("Hello" + Name + "! you have reached the far far away land!")

# chosendoor= None
# sword = None
# while True:
#     chosendoor = input("You see two doors ahead of you! You have to chose left or right. 1").lower()
#     if chosendoor == "right":
#         desicionright = input("""Good job, you have reached the right room. 
#         Oh ooooh! There's a dragon in this room, do you want to fight or exit the room? """ )
#         if desicionright == "exit":
#             continue
#         if desicionright == "fight":
#             if sword != True:
#                 exit = input(" You tried to fight the dragon without a weapon. That was brave, but unfortunately the dragon got the best of you. You died. Do you want to play again? Yes or No")
#                 if exit == "No":
#                     break
#                 if exit == "Yes":
#                     continue
#             if sword == True:
#                 print("""You beat the dragon!! You are now safe. 
#                 You won!!!""")
#                 break
#     if chosendoor == "left":
#         desicionleft = input("You have choices to make. Do you want to look arround or exit the room? 1 ")
#         if desicionleft == "look around":
#             takesword = input("Looks like you found a sword! do you want to take it? Yes or No?")
#             if takesword == "Yes":
#                 sword = True
#             if takesword == "No":
#                 pass
#             continue
#         if desicionleft == "exit":
#             continue
