# Write a lambda expression that takes in three numbers
# and returns the sum of the numbers.

n1 = int(input("give me one number"))
n2 = int(input("give me another number"))
n3 = int(input("give me another number"))


number = lambda x,y,z: x+y+z

print(number(n1,n2,n3))
