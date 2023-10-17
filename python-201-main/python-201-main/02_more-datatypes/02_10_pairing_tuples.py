# The import below gives you a new random list of numbers,
# called `randlist`, every time you run the script.
#
# Write a script that takes this list of numbers and:
#     - sorts the numbers
#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
#
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.
#
# Note: This lab might be challenging! Make sure to discuss it 
# with your mentor or chat about it on our forum.

from resources import randlist

print(randlist)

# Write your code below here
randlist.sort()
print(randlist)
newlist= []
newlist2 = []

# counter=0
# for i in randlist:
#     counter += 1
#     if counter % 2:

if len(randlist) % 2 != 0:
    randlist.append(0)

print(randlist)


for i in range(0,len(randlist),2):
    newlist.append(randlist[i:i+2])

print(newlist)

for i in newlist:
    newlist2.append(tuple(i))
print(newlist2)


