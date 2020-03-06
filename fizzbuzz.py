class FizzBuzz:

    @staticmethod
    def fizzbuzz(number):
        return 'fizzbuzz' if number % 3 == 0 and number % 5 == 0 else \
            ('fizz' if number % 3 == 0 else
                ('buzz' if number % 5 == 0 else
                    ''))
