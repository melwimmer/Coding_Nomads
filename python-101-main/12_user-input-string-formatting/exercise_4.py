word = "hello"

for char in word:
    if char in "aeiou":
        break
    print(char)

print("done")

word = "hello"

for char in word:
    if char in "aeiou":
        continue
    print(char)

print("done")

