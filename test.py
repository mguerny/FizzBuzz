import unittest
from fizzbuzz import FizzBuzz


class TestFizzBuzz(unittest.TestCase):

    def test_should_print_nothing_if_not_multiple_of_3_or_5(self):
        self.assertEqual(FizzBuzz.fizzbuzz(), '')

    def test_should_print_fizz_if_multiple_of_3(self):
        self.assertEqual(FizzBuzz.fizzbuzz(), 'fizz')

    def test_should_print_buzz_if_multiple_of_5(self):
        self.assertEqual(FizzBuzz.fizzbuzz(), 'buzz')

    def test_should_print_fizzbuzz_if_multiple_of_3_and_5(self):
        self.assertEqual(FizzBuzz.fizzbuzz(), 'fizzbuzz')


if __name__ == '__main__':
    unittest.main()

