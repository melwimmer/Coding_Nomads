# Write a script that takes a string from the user
# and creates a list that contains a tuple for each word.
# For example:

input = "hello world"
new_list= []
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

input_list = input.split()
print(input_list)

for i in input_list:
    new_list.append(tuple(i))
    print(type(new_list))
    
print(new_list)

for i in new_list:
    print(type(i))