# Write a decorator that literally decorates text output.
# Make it so the symbol it uses can be an argument to the decorator
#
# The output of a function that returns `"Hello"` that has been
# decorated like with `@decorate("*")` should look like this:
#
# ******************************
# Hello
# ******************************

def decorator(initial_function):
    def wrapper(msg):
        dec = f'''*************
{initial_function(msg)}
************* '''
        return dec
    return wrapper

@decorator
def text_to_be_decd(text):
    return text

input_text = input("Say something: ")

print(text_to_be_decd(input_text))