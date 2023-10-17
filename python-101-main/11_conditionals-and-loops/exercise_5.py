s = "HELLO"
alt_s = ""

for char in s:
    if char in s[1::2]:
        alt_s += char.upper()
    elif char in s[::2]:
        alt_s += char.lower()
    
print(alt_s)
print('@@@@@@@@@@@@@@@@@')


m = "Hello"
alt_sol = ""
for i in range(len(m)):
    if not i%2:
        alt_sol += m[i].upper()
    else:
        alt_sol += m[i].lower()

print(alt_sol)

