import pytest
import unittest

# In terminal type 'pip install unittest'
# In terminal type 'pip install pytest' - normally unittest installs when you type this one in

from simple_calc import SimpleCalc

class Calctest(unittest.TestCase):
# .TestCase is a class that will help us write the test easily

    calc = SimpleCalc() # Object
# Create a funciton for the testcase
    def test_add(self):
        # naming convention is essential as 'test' the word that we need use when naming tests so python interpreter recognises it to run tests
        self.assertEqual(self.calc.add(2, 4), 6) # .assertEqual() = helps us check the value provided, are they working
    # self.calc.add is what we are adding - 2 + 4 = 6 to see if that passes

    def test_substract(self):
        self.assertEqual(self.calc.substract(4, 2), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 2), 4)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)

