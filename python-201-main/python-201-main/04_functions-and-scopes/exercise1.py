def greet(greeting, name):
    sentence = f"{greeting}, {name}! How are you?"
    return sentence

print(greet("Hello", "Martin"))

# def greet(greeting="Hi", name="User"):  # Adding defaults
#     sentence = f"{greeting}, {name}! How are you?"
#     return sentence

# print(greet())
# print(greet(name="Fievel", greeting="Hello"))
