# Hard-code a word that needs to be guessed in the script
# Print an explanation to the user
# Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"
# Ask for user input
# Allow only single-character alphabetic input
# Create a counter for how many tries a user has
# Keep asking them for their guess until they won or lost
# When they find a correct character, display the blank with the word
#   filled in, e.g.: "_ e _ _ _" if they guessed "e" from "hello"
# Display a winning message and the full word if they win
# Display a losing message and quit the game if they don't make it

from operator import index


word = input("Please give me a word: ")

result= " ".join(word)
word_in_list = list(word)


# print("This is hangman. You will have a 15 tries to guess the correct letter. You can yonly guess one letter at a time. Your word is the following:")
hangman = ""       
for i in range(0,len(word)-1):
    hangman += "_ "
hangman += "_"
list_hangman = list(hangman)

# hangman2 = None
# complete_answer = "a m b e r"
# status = False
# print(hangman)


# counter = 0
# letters_found = ""
# while counter < 10:
#     counter += 1
#     print("Tries: " + str(counter))
#     print(hangman)
#     chosen_letter = input("Choose a letter ")
#     for i in word:
#         if chosen_letter == i:
#             letters_found += i
#             print("Letter's you've guessed: " + letters_found + " ")
#             position = (word.index(i))
#             hangman2 = hangman[:position + position:] + chosen_letter + hangman[position + 1 + position:]
#             hangman = hangman2 
#             print(hangman2)
#     if hangman2 == complete_answer:
#         status = True
#         print("you won")
#         break

# else:
#     print("you lost")





counter = 0
letters_found = ""
while counter < 10:
    counter += 1
    print("Tries: " + str(counter))
    letter =input("Choose a letter ")
    for i in range(0,len(word)):
        list_of_idexes = []
        if letter == word_in_list[i]:
            list_of_idexes.append(i)
        for j in list_of_idexes:
            list_hangman[j+j] = letter
        str_list_hangman = "".join(list_hangman)
    if str_list_hangman == result:
            print(str_list_hangman)
            print("You win this time")
            print(f'The word was: {word}')
            break
        
    
    print(str_list_hangman)
else:
     print("You lost")  
    




# name = 'codingnomads'
# new_name = name[:8] + 'rmals'  # using string slicing and concatenation
# print(name, new_name)

# # After re-assigning the value, the old 'name' is overwritten
# name = new_name
# print(name, new_name)
# + hangman[position + 1 + position:]
#hangman[:position + position:] +

