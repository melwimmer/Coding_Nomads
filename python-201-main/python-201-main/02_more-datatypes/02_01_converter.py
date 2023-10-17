# Convert a string to a tuple and print out the result.
# What do you see?
# What happens if you try to iterate over your tuple of characters?
# Do you notice any difference to iterating over the string?

string = "codingnomads"
string2 = "meme"

string = tuple(string)
print(type(string))
print(string)
for i in string:
    print(i.upper())
print(string)
string2 = (string2,)
print(type(string2))
for i in string2:
    print(i.upper())
print(string2)