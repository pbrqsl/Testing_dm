from src.fizz_buzz import FizzBuzz


class TestFizzBuzz:
    def test_should_return_fizz_when_divisible_only_by_3(self):
        number = 6
        expected = "Fizz"
        assert FizzBuzz.fizzbuzz(number) == expected

    def test_should_return_buzz_when_divisible_only_by_5(self):
        number = 10
        expected = "Buzz"
        assert FizzBuzz.fizzbuzz(number) == expected

    def test_should_return_fizzbuzz_when_divisible_by_3_and_by_5(self):
        number = 30
        expected = "FizzBuzz"
        assert FizzBuzz.fizzbuzz(number) == expected

    def test_should_return_nothing_when_disible_neither_by_3_nor_by_5(self):
        number = 7
        expected = None
        assert FizzBuzz.fizzbuzz(number) == expected
