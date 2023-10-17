# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.




chosen_number = int(float(input("choose a number between 0 and 1,000,000,000 ")))
n = 0
while n <= 1000000000:
    if n == chosen_number: 
        break
    else:
        n += 1 
        continue

print(n)


