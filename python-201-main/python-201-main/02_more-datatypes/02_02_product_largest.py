# Take in a few numbers from the user and place them in a list.
# If you want, you can instead use the provided randomly generated
# list called `randlist` to simulate the user input.
#
# Find the largest number in the list and print the result.
# Calculate the product of all of the numbers in the list.

from resources import randlist
import math

print(randlist)
numbers_list = []

counter = 0
while counter <= 5:
    counter += 1
    numbers_list.append(int(input("Tell me a number")))

print(numbers_list)


print(max(numbers_list))
print(sum(numbers_list))
print(math.prod(numbers_list))
