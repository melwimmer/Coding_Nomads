# def outer_func():
#     msg = "Weeeeeekend!"
#     def inner_func():
#         print(msg)
#     return inner_func

# outer_func()()

def outer_fun(msg):
    def inner_fun():
        print(msg)
    return inner_fun

say_wee = outer_fun("fun dun fun")
say_wee()
outer_fun("fun fun fun")()  # OUTPUT: weee