# Write a script that demonstrates a try/except/else statement.
# For example, you can revisit the course module about database interactions
# and include a try/except/else statement based on what to do whether or not
# the database connection can be established.


try:
    dividend = int(input("Please enter the number to be divided: "))
    divisor = int(input("Please enter the divisor: "))
    result = dividend / divisor
except ZeroDivisionError:
    print("My most sincere apologies, but you can't divide by zero.")
except ValueError:
    print("I am once again asking you to use only digits in your input.")
else:
    print(f"The result of {dividend} divided by {divisor} is {result}")