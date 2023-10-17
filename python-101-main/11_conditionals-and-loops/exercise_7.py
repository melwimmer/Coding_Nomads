s = "Hello"
m = ""
counter = 0
for char in s:
    if counter % 2:
        m += char.upper()
    elif not counter %2:
        m += char.lower()
    counter += 1
print(m)
    #print(char, counter)