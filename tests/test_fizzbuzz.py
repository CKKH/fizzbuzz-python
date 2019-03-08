import unittest
from src.fizzbuzz import fizzbuzz

class TestFizzbuzz(unittest.TestCase):
    def test_fizzbuzz_1_returns_buzz(self):
        """ Fizzbuzz(1) return 'buzz' """

        self.assertEqual(fizzbuzz(1), 1)

    def test_fizzbuzz_3_returns_fizz(self):
        """ Fizzbuzz(3) returns fizz """

        self.assertEqual(fizzbuzz(3), 'fizz')

    def test_fizzbuzz_5_returns_buzz(self):
        """ Fizzbuzz(5) return 'buzz' """

        self.assertEqual(fizzbuzz(5), 'buzz')

    def test_fizzbuzz_15_returns_fizzbuzz(self):
        """ Fizzbuzz(15) returns 'fizzbuzz' """

        self.assertEqual(fizzbuzz(15), 'fizzbuzz')

if __name__ == '__main__':
    unittest.main()
