# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.

selected_number = int(input("choose a number between 1 and 1000000000 "))

if selected_number % 3 == 0: 
    print(selected_number)
else:
    print("not divisible by 3")
    