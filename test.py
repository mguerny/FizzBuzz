import unittest
from fizzbuzz import FizzBuzz


class TestFizzBuzz(unittest.TestCase):

    def test_should_print_nothing_if_not_multiple_of_3_or_5(self):
        self.assertEqual(FizzBuzz.fizzbuzz(2), '')

    def test_should_print_fizz_if_multiple_of_3(self):
        self.assertEqual(FizzBuzz.fizzbuzz(3), 'fizz')

    def test_should_print_buzz_if_multiple_of_5(self):
        self.assertEqual(FizzBuzz.fizzbuzz(5), 'buzz')

    def test_should_print_fizzbuzz_if_multiple_of_3_and_5(self):
        self.assertEqual(FizzBuzz.fizzbuzz(15), 'fizzbuzz')


if __name__ == '__main__':
    unittest.main()

