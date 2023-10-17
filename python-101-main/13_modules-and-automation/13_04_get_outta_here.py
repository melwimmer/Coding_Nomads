# Use the built-in `sys` module to explicitly quit your script.
# Include this functionality into a loop where you're asking the user
# for input in an infinite `while` loop.
# If the user enters the word "quit", you can exit the program
# using a functionality provided by this module.

import sys


user_input2 = None

while user_input2 != "quit":
    user_input2 = input("Type someting")
    if user_input2 == "quit":
        sys.exit()    


