# print("{0} is not {1}, but it's {0}!".format("Basil", "Sage"))
# print("{1} is not {0}, but it's {1}!".format("Basil", "Sage"))

# print("Welcome to the unfulfilling market!")
# print("Tell us what you want, and we won't have it.")

# food = input("What do you want? ")
# amount = int(input(f"How much of {food}? "))

# print(f"You want {amount} {food}? Sorry, we only have {amount - 1}.")

print("Welcome to the unfulfilling market!")
print("Tell us what you want, and we won't have it.")

food = input("What do you want? ")
amount = int(input(f"How much of {food}? "))

print("You want {0} {1}? Sorry, we only have {2}.".format(amount, food, amount - 1))