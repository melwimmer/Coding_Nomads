# def decorator_func(initial_func):
#     def wrapper_func():
#         print("the wrapper function picked some...")
#         return initial_func()
#     return wrapper_func # returns the wrapper func ready to be executed

# def prettify():
#     print("flowers for you")

# decorated_pretty = decorator_func(prettify) 
# decorated_pretty() 


def decorator_func(initial_func):
    def wrapper_func():
        msg = f"the wrapper function picked some {initial_func()} for you ..."
        return msg
    return wrapper_func # returns the wrapper func ready to be executed

def prettify():
    return "flowers"

def food():
    return "food"


decorated_prettify = decorator_func(prettify)
decorated_food = decorator_func(food)
print(decorated_prettify())
print(decorated_food())




# #THIS IS ANOTHER WAY!! Same as the 1st
# def decorator_func(initial_func):
#     def wrapper_func():
#         print("the wrapper function picked some ")
#         return initial_func()
#     return wrapper_func # returns the wrapper func ready to be executed


# @decorator_func
# def prettify():
#     print("flowers for you")

# def food():
#     return "food"

# prettify()


