# Write a unittest test suite with at least two methods that test
# the functionality of the built-in `math` module.


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
