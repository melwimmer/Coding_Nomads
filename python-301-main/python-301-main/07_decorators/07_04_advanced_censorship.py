# Build on top of the censorship exercise and change your decorator function
# so that you can pass the words it should censor when decorating a function, e.g.:
# `@censor("shoot", "crab")` would censor the words "shoot" and "crab".

def censor_really(*args):
    def censor(text_function):
        def wrapper_function(uncensored_text):
            for word in args:
                if word in text_function(uncensored_text):
                    new_word = word[0] + (len(word) -1)*"*"
                    uncensored_text = uncensored_text.replace(word, new_word)
            return uncensored_text
        return wrapper_function
    return censor



@censor_really("shoot", "pie")
def text_to_be_quoted(text):
    return text

input_text = "shoot! i dropped my pie"

print(text_to_be_quoted(input_text))





# txt = "shoot! i dropped my pie"
# def wrapper_function(text, *args):
#     for word in args:
#         if word in text:
#             new_word = word[0] + (len(word) -1)*"*"
#             text = text.replace(word, new_word)
#     return text


# print(wrapper_function(txt, "shoot", "pie"))
