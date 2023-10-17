# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# their input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.

# counter = 5
# inputlist= []
# counter2 = 0

# while counter >0:
#     userinput = int(input("Give me a number from 1 to 15 if you repeat the numbers more than 5 times you lose."))
#     if userinput not in inputlist:
#         inputlist.append(userinput)
#         counter2 += 1
#         if counter2 == 10:
#             print('you won!')
#             break
        
     
#     else:
#         counter -= 1 
#         print (f"that one was altrady in there, you have {counter} tries left")

counter = 5
inputset= set()
counter2 = 0

while counter >0:
    userinput = int(input("Give me a number from 1 to 15 if you repeat the numbers more than 5 times you lose."))
    if userinput not in inputset:
        inputset.add(userinput)
        counter2 += 1
        if counter2 == 10:
            print('you won!')
            break
        
     
    else:
        counter -= 1 
        print (f"that one was altrady in there, you have {counter} tries left")

print(inputset)