# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings


string_1 = input("Write a word ")
string_2 = input("Write another word ")
string_3 = input("Write a different word ")

if len(string_1) > len(string_2) and len(string_1) > len(string_3):
    print(len(string_1), string_1)
if len(string_2) > len(string_1) and len(string_2) > len(string_3):
    print(len(string_2), string_2)
if len(string_3) > len(string_1) and len(string_3) > len(string_2):
    print(len(string_3), string_3) 