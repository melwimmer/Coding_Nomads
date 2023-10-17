# Write code that removes all duplicates from a list.
# Solve this challenge in two ways:
# 1. Convert to a different data type
# 2. Use a loop and a second list to solve it more manually

list_ = [1, 2, 3, 4, 3, 4, 5]
list1 = set(list_)
newlist=[]

print(list1)

for i in list_:
    if i not in newlist:
        newlist.append(i)

print(newlist)
