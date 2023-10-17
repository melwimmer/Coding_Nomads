# Create a `Planet()` class that models attributes and methods of
# a planet object.
# Use the appropriate dunder method to get informative output with `print()`

class Planet():
    def __init__(self, name, position, color, composition):
        self.name = name
        self.position = position
        self.color = color
        self.composition = composition
    
    def __str__(self):
        return f"{self.name} is a {self.color} {self.composition} planet and is in the {self.position} position from the sun."
    
me = Planet("Mercury", "1", "gray", "rocky")
v= Planet("Venus", 2, "orange", "rocky")
e = Planet("Earth", 3, "blue", "rocky")
ma = Planet("Mars", 4, "red", "rocky")
j = Planet("Jupiter", 5, "orange", "gas")
s = Planet ("Saturn", 6, "yellow", "gas")
u = Planet("Uranus", 7, "blue", "ice")
n = Planet("Neptune", 8, "blue", "ice")

print(n, me, e)


    
