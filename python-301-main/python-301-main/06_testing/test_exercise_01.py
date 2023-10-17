# import unittest
# import your_package_name


# class TestYourPackageName(unittest.TestCase):

#     def test_your_package_name_function_does_what_it_says(self):
#         # Write your specific test case in here
#         pass


#it would work something like this:
# def test_check_equality(self):
#     """Expects the two inputs to be the same."""
#     self.assertEqual(your_package_name.your_function_call(argument), expected_result)


# Another example of a unittest assertion method is self.assertRaises(), 
# which you can use to confirm that a specific exception has been raised by your code:

# def test_raises_error(self):
#     """Expects the defined error to be raised - e.g. here a ValueError."""
#     with self.assertRaises(ValueError):
#         your_package_name.your_function_call(argument)


import unittest
import math

class TestMath(unittest.TestCase):
    def test_floor_rounds_down(self):
        self.assertEqual(math.floor(3.4), 3)
    
    def test_exp_2(self):
        self.assertEqual(math.log10(10),1)

#You can also add the following code to the bottom of your test file (This is to run it directly)
if __name__ == "__main__":
    unittest.main()

# If you add these two lines of code, you can run the test file using the more familiar command 
# you've always used to execute a Python script:

# python test_your_package_name.py
# You can think of adding the line if __name__ == "__main__:" as giving the following instructions to Python:

# if you run this program directly instead of importing it as a module, do the following:

#THIIIIIIIS READ THIS TO RUN!!

# Run with the following command:
# python -m unittest test_your_package_name.py 