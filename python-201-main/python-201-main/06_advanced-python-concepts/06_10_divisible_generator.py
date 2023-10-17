# Create a Generator that loops over the given range and prints out only
# the items that are divisible by 1111.

nums = range(1, 1000000)
numsgen = (x for x in range(1,1000000))
print(numsgen)
for i in numsgen:
    if i % 1111 == 0:
        print(i)
