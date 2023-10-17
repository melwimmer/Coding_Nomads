# Write a script with three classes that model everyday objects.
# - Each class should have an `__init__()` method that sets at least 3 attributes
# - Include a `__str__()` method in each class that prints out the attributes
#     in a nicely formatted string.
# - Overload the `__add__()` method in one of the classes so that it's possible
#     to add attributes of two instances of that class using the `+` operator.
# - Create at least two instances of each class.
# - Once the objects are created, change some of their attribute values.
#
# Be creative. Have some fun. :)
# Using objects you can model anything you want:
# Animals, paintings, card games, sports teams, trees, people etc...


class Animal():
    def __init__(self, name, color, legs):
        self.name = name
        self.color = color
        self.legs = legs
    def __str__(self):
           return(f'This is a {self.color} {self.legs} legged {self.name}')
    
    def __add__(self, other):
        """Combines two ingredients."""
        new_legs = lambda x, y : x if y > x else y
        new_name = self.name + other.name
        new_color = self.color
        return Animal(name=new_name, legs=new_legs(other.legs,self.legs), color=new_color)

class Tree():
    def __init__(self, namet, colort, sizet):
            self.namet = namet
            self.colort = colort
            self.sizet = sizet
    def __str__(self):
           return(f'This is a {self.sizet} {self.colort} {self.namet}')
    
    def color_change(self):
          print("Oops a bucket of paint just fell on your tree, now it's turned pink")
          self.colort = "pink"

class Book():
    def __init__(self, nameb, colorb, sizeb):
            self.nameb = nameb
            self.colorb = colorb
            self.sizeb = sizeb
    
    def __str__(self):
           return(f'This is a {self.sizeb} {self.colorb} {self.nameb}')

cat=Animal("cat", "blue", 4)
octupus = Animal("octupus", "purple", 8)

redwood = Tree("redwood", 'green', "realbig")
lemon = Tree("lemon", "green", "smallish")


oc = octupus.__add__(cat)
print(oc)

lemon.color_change()
print(lemon.colort)

