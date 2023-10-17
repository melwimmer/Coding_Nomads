# Combine the `greet()` function that you developed in the course materials
# with the `write_letter()` function from the previous exercise.
# Write both functions in this script and call `greet()` within `write_letter()`
# to let `greet()` take care of creating the greeting string.

def greet(greeting, name):
    sentence = f"{greeting}, {name}! How are you?"
    return sentence


def write_letter(name, message):
    return(f'''
    {message} 
    Enjoy your vacation {name}. 
    ''')

name2 = "Melanie"

print(greet("Hi", name2))

print(write_letter("Melanie", "It's that time of the year again, where you take a vacation. We will be taking you wherever you want. Please let us know with enough time. "))