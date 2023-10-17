# Create a decorator that censors potentially offensive words from a text.
# For example, assuming that "shoot" was considered an offensive word:
# A function that would normall return this text:
#    "I bumped my toe! Shoot!"
# Would, after decorating it with `@censor()`, return:
#    "I bumped my toe! S****!"

def censor(initial_function):
    def wrapper_function(uncensored_text):
        if "shoot"in initial_function(uncensored_text):
            sensored_text = uncensored_text.replace("shoot", "s****")
        return(sensored_text)
    return wrapper_function



@censor
def text_to_be_quoted(text):
    return text

input_text = input("Say something: ")

print(text_to_be_quoted(input_text))