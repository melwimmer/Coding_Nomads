# A class is a blueprint for an object.
# User-defined types are called classes

# class Ingredient:
#     """Creates an empty Ingredient object."""
#     pass

# i = Ingredient()  # Instantiating an object of the class
# print(type(i))  # OUTPUT: <class '__main__.Ingredient'>


# #assinging a value to a variable inside the instance
# i.name = "carrot"

# print(i.name)

## NOTE: the above method is not what is usually used. We normally do it like this:

# class Ingredient:
#     """Models an Ingredient. Currently only carrots!"""

#     def __init__(self):
#         self.name = "carrot"

# i = Ingredient()
# print(i.name)  # OUTPUT: carrot

# c = Ingredient()
# print(c.name)  

class Ingredient:
    """Models a food item used as an ingredient."""

    def __init__(self, name, amount, color):
        self.name = name
        self.amount = amount
        self.color = color

    def expire(self):
        """Expires the ingredient."""
        print(f"whoops, these {self.name} went bad...")
        self.name = "expired " + self.name

    def use(self, use_amount):
        self.amount -= use_amount
    
    def __str__(self):
        return f"{self.name} ({self.amount})"
    
    def __repr__(self):
        return f"Ingredient(name={self.name}, amount={self.amount})"
    
    def __add__(self, other):
        """Combines two ingredients."""
        new_name = self.name + ' and ' + other.name
        new_amount = self.amount + other.amount
        return Ingredient(name=new_name, amount=new_amount, color = "")



i = Ingredient("peas",23,"green")
c = Ingredient("cauliflower",2,"white")
b = Ingredient("broccoli",2,"green")
d = Ingredient("dandelion",0.5,"yellow")

print(c.name, b.amount, d.color)
print(i.name)

i.expire()
print(i.name)  

c.use(1)
print(c.name,c.amount)

i.use(10)
print(i.name,i.amount)

print(i)

print(repr(i))

bd = b.__add__(d)
print(bd)
