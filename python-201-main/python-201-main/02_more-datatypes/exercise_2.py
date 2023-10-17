bucketlist = ['move to a diferent country', 'be happy', 'be Amma as much as possible', 'go to yosemite', 'see the redwoods', 'swim with whales', 'find a partner']
print(bucketlist[-1])
print(bucketlist[::2])

for item in bucketlist:
    print(item)


bucketlist.append('get a dog')
print(bucketlist)

bucketlist.pop(4) 
print (bucketlist)

yosemite = (bucketlist.pop(3))

print(bucketlist)

bucketlist[2] = "live in the ashram"
print(bucketlist)

bucketlist.remove(bucketlist[4])
print(bucketlist)

numberlist = [1, 2, 3, 2]
print(numberlist * 3)
print(numberlist)
numberlist.remove(2)
print(numberlist)

fruitslist = ["apple", "pear", "banana", "lime"]
fruitslist.insert(3, "cranberry")
print(fruitslist)

fruitslist.sort()
print(fruitslist)