from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

def test_str_():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(2)
    assert str(jar) == "🍪🍪"
    jar.deposit(10)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(4)
    assert jar.size == 9
    with pytest.raises(ValueError):
        jar.deposit(15)
    with pytest.raises(ValueError):
        jar.deposit(-3)

def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(5)
    assert jar.size == 7
    jar.withdraw(6)
    assert jar.size == 1
    with pytest.raises(ValueError):
        jar.withdraw(2)
    with pytest.raises(ValueError):
        jar.withdraw(-3)
