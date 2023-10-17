# Using a loop, sum all numbers from the `start` to the `stop` number.
# The sequence should consist only of integers from 1 to 100.
# The output of your calculation should look like this:
#
#      The sum is: 5050

start = 1
stop = 100
number = 0

for start in range(101):
    number += start
    start += 1  

print(start)
print("The sum is:", + number)   

