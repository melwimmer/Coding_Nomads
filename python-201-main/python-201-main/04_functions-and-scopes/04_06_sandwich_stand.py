# Write a function called `make_sandwich()` that sticks to the following:
# - takes a type of bread as its first, required argument
# - takes an arbitrary amount of toppings
# - returns a string representing a sandwich with the bread on top
#   and bottom, and the toppings in between.

def make_sadwich(bread, *args):
    sandwich = ""
    toppings = ""
    for topping in args:
        toppings += f'{topping} \n' 
    sandwich += f'{bread}\n{toppings}{bread}'
    return(sandwich)

print(make_sadwich("flatbread", "mayo", "cheese","tomato", "lettuce", "sprinkles", "joy"))

