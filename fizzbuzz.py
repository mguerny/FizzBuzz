class FizzBuzz:

    @staticmethod
    def fizzbuzz(number):
        if number % 3 == 0 and number%5 == 0:
            return 'fizzbuzz'
        else:
            if number % 3 == 0:
                return 'fizz'
            else:
                if number % 5 == 0:
                    return 'buzz'
                else:
                    return ''
