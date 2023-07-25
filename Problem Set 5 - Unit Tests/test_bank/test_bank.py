from bank import value
import pytest


def test_hello_in_greeting():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("hello Mike ") == 0


def test_h_is_1st_letter_in_greeting():
    assert value("HI") == 20
    assert value("hey") == 20
    assert value("How are you?") == 20


def test_greeting_without_hello_or_1st_h():
    assert value("Good day!") == 100
    assert value("MY GREETINGS") == 100


def test_without_input():
    with pytest.raises(IndexError):
        value("")
