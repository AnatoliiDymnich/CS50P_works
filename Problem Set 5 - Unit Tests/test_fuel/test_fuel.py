import fuel
import pytest


def test_convert_correct():
    assert fuel.convert("3/4") == 75.0
    assert fuel.convert("0/4") == 0
    assert fuel.convert("4/4") == 100.0


def test_convert_value_error():
    with pytest.raises(ValueError):
        fuel.convert("cat/dog")


def test_convert_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        fuel.convert("4/0")


def test_gauge():
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(50) == "50%"
