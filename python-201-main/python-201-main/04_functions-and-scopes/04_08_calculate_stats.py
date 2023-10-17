# Write a function named `stats()` that takes in a list of numbers
# and finds the maximum, minimum, average and sum of the numbers.
# Print these values to the console you call the function.

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(numberlist):
  maximum = 0
  minimum = 0
  average = 0
  maximum += max(numberlist)
  minimum += min(numberlist)
  average += sum(numberlist)/len(numberlist)
  return(minimum, maximum, average)

print(stats(example_list))



# call the function below here
