from numb3rs import validate


def test_valid_ip():
    assert validate("127.0.0.1") == True
    assert validate("10.20.30.40") == True
    assert validate("255.255.255.255") == True
    assert validate("1.0.0.0") == True


def test_invalid_ip():
    assert validate("302.10.10.11") == False
    assert validate("1.125.1110.256") == False
    assert validate("456.256.10.11") == False
    assert validate("1.-10.10.11") == False
    assert validate("cat") == False
    assert validate("99.456.10.11") == False
    assert validate("255.255.255.256") == False
