# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.

statement = input("Please write a statement.")
a_ocurrences = statement.count("a")
e_ocurrences = statement.count("e")
i_ocurrences = statement.count("i")
o_ocurrences = statement.count("o")
u_ocurrences = statement.count("u")

print(f"count of a's: {a_ocurrences} \n count of e's: {e_ocurrences} \n count of i's: {i_ocurrences} \n count of o's: {o_ocurrences}\n count of u's: {u_ocurrences}")
