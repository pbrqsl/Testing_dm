import pytest
from src.exercise_8_no_return import show_message

class TestShowMessage:

    def test_should_print_out_given_message(self, capfd):
        show_message('a')
        out, err = capfd.readouterr()
        expected = 'Your message: a\n'
        assert out == expected

    def test_should_print_none(self, capfd):
        show_message(None)
        out, err = capfd.readouterr()
        expected = 'Your message: None\n'
        assert out == expected
