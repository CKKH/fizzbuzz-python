import unittest

from src.fizzbuzz import fizzbuzz

class TestFizzbuzz(unittest.TestCase):
    def test_fizzbuzz_3_returns_fizz(self):
        """ Fizzbuzz(3) returns fizz """

        result = fizzbuzz(3)
        self.assertEqual(result, 'fizz')

    def test_fizzbuzz_6_returns_fizz(self):
        """ Fizzbuzz(6) returns fizz """

        result = fizzbuzz(6)
        self.assertEqual(result, 'fizz')

    def test_fizzbuzz_10_returns_buzz(self):
        """ Fizzbuzz(10) retusn 'buzz' """

        result = fizzbuzz(10)
        self.assertEqual(result, 'buzz')

if __name__ == '__main__':
    unittest.main()
