fruitsa = set(["apple", "banana", "grape", "tomato", "banana"])
fruitsb = set(["papaya", "anona", "banana"])

fruitsc = fruitsa.union(fruitsb)
print(fruitsc)

fruitsa.update(fruitsb)
print(fruitsa)