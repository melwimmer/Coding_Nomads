# Using a `for` loop, print out all odd numbers from 1 to 100.
number = 0

for i in range(100):
    number += 1
    if number % 2 != 0:
        print (number)