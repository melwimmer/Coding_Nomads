# Collect user input
# NEW --> Convert user input to lowercase
# Compare to the string "something"
# Print a win or lose message
word = input ("Write something to win ")
word = word.lower()
if (word == 'something'): 
    (print("you win!"))
else: 
    print("wrooong!")

