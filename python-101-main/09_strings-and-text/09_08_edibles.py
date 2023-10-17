# Extract four words of edible food items from the sentence below.
# Use only string slicing to pick them out!
# Feel free to use pen and paper to number the indices
# and find the locations quicker.
#
# What dish can you make from these ingredients? :)

s = "They grappled with their leggins before going to see the buttercups flourish."
print((len(s)))
# 0:they 5:grappled 14:with 19:their 25: leggins 33: before 40:
s0 = "They"
print(s[7:12])
print(s[26:29])
print(s[57:63])
print(s[68:73])
print(s.count(s0, 0, 12))
print(s.find("flour"))
print(s.startswith("They"))
