# try:
#     dividend = int(input("Please enter the number to be divided: "))
#     divisor = int(input("Please enter the divisor: "))
#     result = dividend / divisor
#     print(f"The result of {dividend} divided by {divisor} is {result}")
# except ZeroDivisionError:
#     print("My most sincere apologies, but you can't divide by zero.")
# except ValueError:
#     print("I am once again asking you to use only digits in your input.")
# except Exception as e:
#     print(f"I humbly inform you that {e} has occurred.")


# # ##I can also raise the exception myself
# # age = int(input("Age: "))
# # if age < 0:
# #     raise ValueError("Looks like you're not born yet.")

# class AgeError(Exception):
#     def __init__(self, age):
#         self.age = age

# ## This is 
# age = int(input("Age: "))

# try:
#     if age < 0:
#         raise AgeError(age)
# except AgeError as ae:
#     print(f"Pssst... This might be a miracle. They say they're {ae.age} years old.")


class AgeError(Exception):
    def __init__(self, age):
        self.age = age
        self.message = f"You'll be born in {abs(self.age)} years."


age = int(input("Age: "))

try:
    if age < 0:
        raise AgeError(age)
except AgeError as ae:
    print(ae.message)
