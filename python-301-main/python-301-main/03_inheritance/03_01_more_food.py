# Create another child class that inherits from `Ingredient()`. You can use
# the code you wrote yourself, or continue working with the one provided below.
# Implement at least one extra method for your child class, and override the
# `expire()` method from the parent `Ingredient()` class.

class Ingredient:
    """Models an Ingredient."""

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def expire(self):
        """Expires the ingredient item."""
        print(f"whoops, these {self.name} went bad...")
        self.name = "expired " + self.name

    def __str__(self):
        return f"You have {self.amount} {self.name}."


class Spice(Ingredient):
    """Models a spice to flavor your food."""

    def grind(self):
        print(f"You have now {self.amount} of ground {self.name}.")

#This is inheritace (the child class inherits all the atributes and methods form the parent class. It can also create methods that only work for the child)
class Spice(Ingredient):
    def grind(self):
        print(f"You have now {self.amount} of ground {self.name}.")

    def roast(self):
        print(f"You have now {self.amount} of roasted {self.name}.")

    def expire(self):
        if self.name == "salt":
            self.name = "salt"
            print(f"Silly, salt doesn't expire")
        else:
            self.name = "old " + self.name
            print(f"your {self.name} has expired. it's probably still good.")
# now say that what I want is to add an atribute but only for spices (the child class and not the parent class (Ingredient)) then I can do something
#like this: I call super which gives you access to the contents of your parent class. And just like you would with any other method, you then 
# explicitly call the .__init__() constructor of the parent class, passing it the two arguments that it requires.
    def __init__(self, name, amount, taste):
        super().__init__(name, amount)
        self.taste = taste
        

class Vegetable(Ingredient):
    def chop(self):
        self.name = 'chopped ' + self.name
        print(f'You now have {self.amount} of {self.name}')
        


p = Ingredient('peas', 12)
print(p)  # OUTPUT: You have 12 peas.
s = Spice('salt', 200, "salty")
pe = Spice('pepper', 40, "spicy")
print(s)  # OUTPUT: You have 200 salt.
c=Vegetable('carrot', 50)

s.grind()

p.expire()
s.expire()
c.expire()
c.chop()

print(pe.taste)

print(p,s,c)