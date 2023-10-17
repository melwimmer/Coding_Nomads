# Write a decorator function that wraps text output into quotes, e.g.:
# Hello world! ----> "Hello World!"
# You can use it to create quotes from text output.


def outer_function(initial_function):
    def wrapper_function(msg):
        quoted_text = f'"{initial_function(msg)}"'
        return quoted_text
    return wrapper_function

@outer_function
def text_to_be_quoted(text):
    return text

input_text = input("Say something really smart so it can be quoted")

print(text_to_be_quoted(input_text))


# #I can also do:
# def outer_function(initial_function):
#     def wrapper_function(msg):
#         print(f'"{initial_function(msg)}"')
#         return initial_function
#     return wrapper_function

# @outer_function
# def text_to_be_quoted(text):
#     return text

# input_text = input("Say something really smart so it can be quoted")

# text_to_be_quoted(input_text)