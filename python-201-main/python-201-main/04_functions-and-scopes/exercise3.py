def greet_many(greeting, *args):
    greetings = ""
    for name in args:
        sentence = f"{greeting}, {name}! How are you?"
        greetings += sentence + "\n"
    return greetings


print(greet_many("hello", 'mary','luis', 'melanie', 'blabla'))

# def greet_many(**kwargs):
#     greetings = ""
#     for greeting, name in kwargs.items():
#         sentence = f"{greeting}, {name}! How are you?"
#         greetings += sentence + "\n"
#     return greetings


# print(greet_many(hi = 'melanie', hello = 'anthony'))