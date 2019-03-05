import unittest

from src.fizzbuzz import fizzbuzz

class TestFizzbuzz(unittest.TestCase):
    def test_fizzbuzz_return(self):
        """ Test that fizzbuzz returns fizzbuzz """

        result = fizzbuzz()
        self.assertEqual(result, 'fizzbuzz')

if __name__ == '__main__':
    unittest.main()
