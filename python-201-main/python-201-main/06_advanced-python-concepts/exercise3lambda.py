#esto:
def square_root(x):
    return x**2

print(square_root(5))
#es lo mismo que esto:

squared = lambda x: x**2
print(squared(5))

#More examples of lambda functions

ingredients = [("carrots", 2), ("potatoes", 4), ("peppers", 1)]
print(sorted(ingredients, key=lambda x: x[1]))

#More examples of lambda functions but thisone is not practical.
squares = list(map(lambda x: x**2, range(10)))
print(squares)  # OUTPUT: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
