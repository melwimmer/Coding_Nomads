# Write a program with three functions. Each function must call
# at least one other function and use the return value
# of that function to do something with it. You can have more
# than three functions, and they don't need to call each other
# in a circular way.

# def age():
#     userage = input("How old are you?")
#     return(userage)


def greeting(name):
    def age():
        userage = int(input("How old are you? "))
        return(userage)
    def present():
        userpresent = (input("The company is allowing you to choose between a unicorn, chocolate and a goblin. Choose one present: "))
        return(userpresent)
    greet = f" Congrats {name} you're turning {age()}. The company will be sending you a {present()} !!"
    return(greet)

print(greeting("Melanie"))

