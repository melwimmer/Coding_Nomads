# Adapt your Generator expression from the previous exercise:
# Add a floor division by 1111 on it.
# What numbers do you get?

nums = range(1, 1000000)
numsgen = (x for x in range(1,1000000))
print(numsgen)
for i in numsgen:
    if i % 1111 == 0:
        print(i//1111)
        

