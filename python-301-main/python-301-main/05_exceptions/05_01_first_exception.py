# Write a script that generates an exception.
# Handle this exception with a try/except block.
# For example:
#
# list_ = ["hello world!"]
# print(list_[1])
#
# This raises and exception that needs to be handled.

try:
    list_ = ["hello world!"]
    print(list_[1])
except IndexError:
    print("You are probably not using a 0 index! try that and come again!")