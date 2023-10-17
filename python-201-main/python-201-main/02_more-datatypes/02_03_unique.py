# Write code that creates a list of all unique values in a list.
# For example:
#
# list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
# unique_list = [55, 'hi', 4, 13]
original_list=[1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
list_1 =[1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
newlist= []

#this didn't work

# for i in list_1:
#     if i not in newlist:
#         newlist.append(i)

# for i in list_1:
#     if i in newlist:
#         list_1.remove(i)
#         newlist.remove(i)
        
# print(newlist)
# print(list_1)


for i in original_list:
    if original_list.count(i) == 1:
        newlist.append(i)

print(newlist)