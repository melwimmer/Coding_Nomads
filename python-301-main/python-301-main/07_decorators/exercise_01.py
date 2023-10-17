def lowercase(func):
    """A decorator that avoids digital screaming."""
    def wrapper(text):
        initial_result = func(text)
        new_result = initial_result.lower()
        return new_result
    return wrapper

@lowercase
def say_something(text):
    return text

string = "I LOVE COWS"
@lowercase
def cows(text):
    return text[-4:]

print(say_something("HEI WHAT'S UP?"))  # OUTPUT: hei what's up?
print(cows(string))


def say_hi():
    print("Hi.")

def say_moo():
    print("moooooooo!")

function_list = [say_hi, say_moo]
print(function_list[0])
function_list[0]()

function_list1 = [say_hi(),say_moo()]
print(function_list1[0])