# Test Driven Development 
# Pytest and Unittest
## Use pip to install the packages
## TDD

The idea is that nothing is sent to production before it is tested. Using a car as an example, a tire for the car may be made separately. If the main manufacturer sends specifications such as the top speed the tire would need to be able to withstand for some amount of time. The same might happen with the brakes. This would happen for all components in the car.

Similarly, in TDD, we write tests for our software first, then focus on passing those tests with our code to ensure we deliver what the product owner has asked for.

TDD
- Starts with RED everything failing before writing functional code to pass tests
- GREEN write or refactor the code to pass test
- BLUE Refactoring - start again with next tests
`unittest` and `pytest`
  
Naming convention'
"test" is an important keyword and is necessary for pytest to recognise functions designed to test

## Writing Tests
```python
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

```
SimpleCalc can be found here:
```python
class SimpleCalc:

    def add(self, int1, int2):
        return int1 + int2

    def substract(self, int1, int2):
        return int1 - int2

    def multiply(self, int1, int2):
        return int1 * int2

    def divide(self, int1, int2):
        return int1 / int
```

Test-Driven Development
Running this file's tests will attempt to run the corresponding, and return information on the success or failure of these functions.

Having written the tests for the software, we can now write code to satisfy our test cases. In this case, I used the calculator programmed as part of the object-oriented programming exercise to attempt to satisfy the tests. Once the tests are passed, we refactor our code, and design further tests if necessary.


