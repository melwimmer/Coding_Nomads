# Write a script that takes the following two dictionaries
# and creates a new dictionary by combining the common keys
# and adding the values of duplicate keys together.
# Use `for` loops to iterate over these dictionaries
# to accomplish this task.
#
# Example output:
# result = {"a": 3, "b": 2, "c": 7 , "d": 2}

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}
dict_3 = {}


for letter in dict_1.keys():
    if letter not in dict_2:
        dict_3[letter] = dict_1.get(letter)
    else:
        dict_3[letter] = dict_1.get(letter) + dict_2.get(letter)

for letter in dict_2.keys():
    if letter not in dict_1:
        dict_3[letter] = dict_2.get(letter)

print(dict_3)

