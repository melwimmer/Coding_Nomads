# Write a script that creates a dictionary of keys, `n`
# and values `n * n` for numbers 1 to 10. For example:
# result = {1: 1, 2: 4, 3: 9, ... and so on}

counter = 0

n = 20
numdict = {}

while counter <= (n-1):
    counter += 1
    numdict[counter] = counter*counter

print(numdict)

