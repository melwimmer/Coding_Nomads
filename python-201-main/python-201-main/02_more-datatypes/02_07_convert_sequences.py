# Convert some sequences you got to know into other sequences:
# - Convert the string shown below into a tuple.
# - Convert the tuple into a list.
# - Change the `c` character in your list into a `k`
# - Convert the list back into a tuple.

string = "codingnomads"
tupstring= tuple(string)
print(tupstring)
listtupstring= list(tupstring)
print(listtupstring)
listtupstring[0] = "k"
print(listtupstring)
tupstring2 = tuple(listtupstring)
print(tupstring2)