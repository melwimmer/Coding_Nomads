# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.
#future = present x (1 +i)^n

investment_ammount = int(input(" What is the investment amount? "))
interest_rate_in_percentage = int(input( "what is the interest rate in percentage? " ))
number_of_years_to_invest = int(input("what is the number of years to invest? " ))

print(f'the future investment is {investment_ammount*(1+interest_rate_in_percentage)**number_of_years_to_invest}')
