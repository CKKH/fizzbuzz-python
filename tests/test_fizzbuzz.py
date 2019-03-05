import unittest

from src.fizzbuzz import fizzbuzz

class TestFizzbuzz(unittest.TestCase):
    def test_fizzbuzz_returns_number(self):
        """ Fizzbuzz returns 3 """

        result = fizzbuzz(3)
        self.assertEqual(result, 'fizz')

if __name__ == '__main__':
    unittest.main()
