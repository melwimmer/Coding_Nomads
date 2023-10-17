# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4

# string_input = input("Type something with an 'o' ")
# print(string_input.find("o"))


word= "amber"
letters_found= ""
while letters_found != "amber":
    selected_letter= input("Choose a letter")
    for char in word:
        if char != selected_letter:
            break
        else:
            letters_found += selected_letter
            print(letters_found)
    else:
        break





    