import random

class Pokemon():
    def __init__(self, name, primary_type, max_hp, hp):
        self.name = name
        self.primary_type = primary_type
        self.max_hp =max_hp
        self.hp = hp

    def battle(self, other):
        self.primary_type
        other.primary_type

        print(f'{self.name} is a {self.primary_type} and {other.name} is a {other.primary_type}')
        
        if self.primary_type == other.primary_type:
            print(f"Both players selected {other.primary_type}. It's a tie!")
        elif self.primary_type == "water":
            if other.primary_type == "fire":
                print(f"{self.name} wins, {other.name} has lost 3 hp")
                other.hp -= 3
                print(f'{self.name} hp = {self.hp} and {other.name} hp = {other.hp}')
            else:
                print(f"{other.name} wins, {self.name} has lost 3 hp")
                self.hp -=3
                print(f'{self.name} hp = {self.hp} and {other.name} hp = {other.hp}')
        elif self.primary_type == "grass":
            if other.primary_type == "water":
                print(f"{self.name} wins, {other.name} has lost 3 hp")
                other.hp -= 3
                print(f'{self.name} hp = {self.hp} and {other.name} hp = {other.hp}')
            else:
                print(f"{other.name} wins, {self.name} has lost 3 hp")
                self.hp -=3
                print(f'{self.name} hp = {self.hp} and {other.name} hp = {other.hp}')
        elif self.primary_type == "fire":
            if other.primary_type == "grass":
                print(f"{self.name} wins, {other.name} has lost 3 hp")
                other.hp -= 3
                print(f'{self.name} hp = {self.hp} and {other.name} hp = {other.hp}')
            else:
                print(f"{other.name} wins, {self.name} has lost 3 hp")
                self.hp -=3
                print(f'{self.name} hp = {self.hp} and {other.name} hp = {other.hp}')

    def feed(self):
        self.hp +=5

    
p1 = Pokemon("Charmander", "fire", 150, 150)
p2 = Pokemon("Bulbasuaur", "grass", 150, 150)
p3 = Pokemon("Squirtle", "water", 150, 150)


p1.battle(p2)
