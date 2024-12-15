import unittest
from Calculator import Calculator

class TestFactorial(unittest.TestCase):

    def test_factorial(self):
        calc = Calculator()
        self.assertEqual(calc.factorial(5), 120)
        self.assertEqual(calc.factorial(0), 1)
        self.assertEqual(calc.factorial(1), 1)
        with self.assertRaises(ValueError):
            calc.factorial(-5)

if __name__ == "__main__":
    unittest.main()
