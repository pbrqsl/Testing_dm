from src.exercise_1_prime_numbers import Prime
import pytest

class TestPrime:

    def test_should_retuern_false_for_1(self):
        number = 1
        expected = False
        assert Prime.is_prime(number) is expected

    def test_should_return_true_for_3(self):
        number = 3
        expected = True
        assert Prime.is_prime(number) is expected

    def test_should_return_false_for_4(self):
        number = 4
        expected = False
        assert Prime.is_prime(number) is expected

    def test_should_return_false_for_negative(self):
        number = -7
        expected = False
        assert Prime.is_prime(number) is expected

    def test_should_return_false_for_non_int(self):
        number = 0.23
        expected = False
        assert Prime.is_prime(number) is expected
