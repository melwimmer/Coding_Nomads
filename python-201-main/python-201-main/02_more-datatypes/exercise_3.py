names = ["Ada", "Bertha", "Carol"]
lowercase_names = [x.lower() for x in names]
print(lowercase_names)

#That is the same as doing this:

names2 = ["Ada", "Bertha", "Carol"]

lowercase_names2 = []
for x2 in names2:
    lowercase_names2.append(x2.lower())

print(lowercase_names2) 