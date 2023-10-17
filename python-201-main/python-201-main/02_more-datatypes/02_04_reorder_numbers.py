# Read in 10 numbers from the user.
# Place all 10 numbers into an list in the order they were received.
# Print out the second number received, followed by the 4th, 
# then the 6th, then the 8th, then the 10th.
# Then print out the 9th, 7th, 5th, 3rd, and 1st number:
#
# Example input:  1,2,3,4,5,6,7,8,9,10
# Example output: 2,4,6,8,10,9,7,5,3,1


numbers_list = []
new_list=[]

counter = 0
while counter <= 9:
    counter += 1
    numbers_list.append(int(input("Tell me a number")))

print(numbers_list)


for i in numbers_list[1::2]:
    new_list.append(i)

for i in numbers_list[8::-2]:
    new_list.append(i)

print(new_list)



