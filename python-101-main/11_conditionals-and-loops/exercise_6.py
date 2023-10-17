s = "Hello"
alt_s = ""

for i in range(len(s)):
    if not i%2:
        alt_s += s[i].upper()
    else:
        alt_s += s[i].lower()

print(alt_s)