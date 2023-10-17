# Create a custom decorator function that records the execution time of
# the decorated function and prints the time to your console when the function
# has finished execution.

from datetime import datetime

def log_it(func):
    def wrapper():
        print(f'{func()}')
        print(f"{func.__name__} was called at {datetime.now()}\n")
        return func
    return wrapper

@log_it
def print_hello():
    return "hello!"

print_hello()

####This was an example from coding nomads on how to use a wrapper function to log emails with dates. 
# def log_it(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         with open("activity.log", "a") as f:
#             f.write(f"{func.__name__} was called at {datetime.now()}\n")
#         return result
#     return wrapper

# @log_it
# def send_email(to, subject, message):
#     return f'''{to}
# {subject}
# {message}'''

# send_email("user@example.com", "Hello", "How are you?")


