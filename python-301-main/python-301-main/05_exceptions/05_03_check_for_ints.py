# Create a script that asks a user to input an integer, checks for the
# validity of the input type, and displays a message depending on whether
# the input was an integer or not.
# The script should keep prompting the user until they enter an integer.



while True:
    try:
        number = int(input("Please give me an integer"))
        if type(number) == int:
            break
    except ValueError:
        print("This is not an integer")
          
