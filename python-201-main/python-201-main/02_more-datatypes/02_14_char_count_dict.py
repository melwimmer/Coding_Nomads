# Write a script that takes a text input from the user
# and creates a dictionary that maps the letters in the string
# to the number of times they occur. For example:
#
# user_input = "hello"
# result = {"h": 1, "e": 1, "l": 2, "o": 1}


userinput = 'hello'
user_dict = {}
user_list = []

for i in userinput:
   user_list.append(i)
   user_dict[i]= user_list.count(i) 

print(user_dict)
