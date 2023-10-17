# Ask the user to input their name. Then print a nice welcome message
# that welcomes them personally to your script.
# If a user enters more than one name, e.g. "firstname lastname",
# then use only their first name to overstep some personal boundaries
# in your welcome message.

user_fullname = input("please type your name ")
userfirstname = ""
lastname = False
for char in user_fullname:
    if lastname == False:
        userfirstname += char
    if char == " ":
        lastname = True
        
print(userfirstname)



