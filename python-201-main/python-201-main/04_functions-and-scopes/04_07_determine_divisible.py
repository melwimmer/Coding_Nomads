# Write a script where you complete the following tasks:
# - define a function that determines whether the number is
#   divisible by 4 OR 7 and returns a boolean
# - define a function that determines whether a number is
#   divisible by both 4 AND 7 and returns a boolean
# - take in a number from the user between 1 and 1,000,000,000
# - call your functions, passing in the user input as the arguments,
#   and set their output equal to new variables 
# - print your the result variables with descriptive messages

userinput = int(input("Give me a number between 1 and 1,000,000,000"))
print(type(userinput))

def divisible4or7(number):
    variable = None
    if number % 4 == 0 or number %7 ==0:
        variable = True
        print("Your number is divisible by 4 or 7")
    else: 
        variable = False
        print("Your number is not divisible by 4 or 7")
    return(variable)
    

print(divisible4or7(userinput))


def divisible4and7(number):
    variable = None
    if number % 4 == 0 and number %7 ==0:
        variable = True
        print("Your number is divisible by 4 and 4")
    else: 
        variable = False
        print("Your number is not divisible by 4 and 7")
    return(variable)

print(divisible4and7(userinput))