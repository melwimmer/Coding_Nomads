# Define a function called `write_letter()` that takes as input a `name`
# and a `text` argument. In the body of the function, create a greeting
# message with the `name` input, as well as a goodbye message that uses
# the `name` again. Combine that with the input `text` to return a
# complete `letter`.

def write_letter(name, message):
    return(f'''Dear {name},'
    {message} 
    Enjoy your vacation {name}. 
    ''')

print(write_letter("Melanie", "It's that time of the year again, where you take a vacation. We will be taking you wherever you want. Please let us know with enough time. "))