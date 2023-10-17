# Demonstrate your knowledge of unittest by first creating a function 
# with input parameters and a return value.
# Once you have a function, write at least two tests for the function 
# that use different assertions. The tests should pass.
# Then, include another test that doesn't pass.
#
# NOTE: You can write both the code as well as the tests for it in this file.
# However, feel free to adhere to best practices and separate your tests and
# the functions you are testing into different files.
# Keep in mind that you will run into an error when you'll attempt to import
# this file, because Python modules can't begin with a number.
# You can rename the file to make it work :)

farm_animals = ["alpaca.jpg", "dog.py", "cat.xls", "anaconda.jpg"]
jpg_farm_animals = []

def animals_start_with_a(animal_list,empty_list):
    for i in animal_list:
        if i.endswith(".jpg"):
            empty_list.append(i)
    return empty_list