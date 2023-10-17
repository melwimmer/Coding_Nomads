# Take in a number between 1 and 12 from the user
# and print the name of the associated month:
# "January", "February", ... "December"
# Print "Error" if the number from the user is not between 1 and 12.
# Use a nested `if` statement.

# My solution

month = int(input("chose a number between 1 and 10"))
monthlist = ["Jan", "Feb", "Mar", "Ap", "May",  "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec" ]

if month > 0 and month <13:
    print(monthlist[month-1])
else:
    print("error")

#The solution with nested if

# month = int(input("chose a number between 1 and 10"))
# monthlist = ["Jan", "Feb", "Mar", "Ap", "May",  "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec" ]

# if month > 0:
#     if month <13:
#         print(monthlist[month-1])
#     else:
#         print("Error")
# else:
#     print("Error")
