# Proof that the following file is a .pdf file using a `for` loop.
# - Don't use the string method you've used to solve this before!
# - Don't use the `in` keyword to look for a sub-string!
# - Don't use any string slicing technique either!
#
# You'll see that it'll be tricky to solve this challenge with a loop :)
# Remember to use also other techniques you've learned,
# for example flags and conditional statements.

filename = "operators.pdf"
extension = False
file = ""
for char in filename:
    if char == ".":
        extension = True
    if extension == True:
        file += char
if file == "pdf":
    print("It's a pdf")




        








    

    

# pdf = ""
# # for i in range(len(filename)): 
# if filename[-3] == 'p' and filename[-2] == 'd' and filename[-1] == 'f':
#     pdf = True
# else:
#     pdf = False

# if pdf == True:
#     print("It's a PDF!!")
# else:
#     print("It's not a PDF")


# (len(filename) - (len(filename) - 3))

# filename = "operators.pdf"

# pdf = ""
# for char in range((len(filename)-3),  len(filename)): 
# #     if char == "p":
# #         pdf += char
# #     elif char == "d":
# #         pdf += "d"
# #     elif char == "f":
# #         pdf += "f"
# #     else:
# #         print("Not a pdf")
# 

# print(pdf)

# filename = "operators.pdf"

# pdf = ""

# for i in range((len(filename)-3),  len(filename)): 
#     for i in filename:
#         if i == "p":
#             pdf += "p"
#         elif i == "d":
#             pdf += "d"
#         elif i == "f":
#             pdf += "f"
        

# print(pdf)

# filename = "operators.pdf"

# pdf = ""

# for i in filename: 
#     #for i in range((len(filename)-3),  len(filename)):
#     if i == "p":
#         pdf += "p"
#     elif i == "d":
#         pdf += "d"
#     elif i == "f":
#         pdf += "f"

# print(pdf)

# if pdf == filename[(len(filename)-3),  len(filename)]:
#     print(True)
    
    



# filename = "operators.pdr"
# pdf = ""

# for i in range(len(filename)): 
#     if filename[-3] == 'p' and filename[-2] == 'd' and filename [-1] == 'f':
#         pdf += "pdf"
#     else:
#         pdf += "not pdf :("



    


