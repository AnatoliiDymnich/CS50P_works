from plates import is_valid


def test_valid_name():
    assert is_valid("CS50") == True
    assert is_valid("ABC123") == True
    assert is_valid("ABCDEF") == True


def test_more_6_characters():
    assert is_valid("XY777YZ") == False


def test_less_2_chracters():
    assert is_valid("F") == False


def test_numbers_in_the_middle():
    assert is_valid("NUM33B") == False


def test_numbers_starts_with_zero():
    assert is_valid("MVP02") == False
    assert is_valid('ABC012') == False


def test_starts_with_numbers():
    assert is_valid("22") == False


def test_punctuation_marks():
    assert is_valid(".,!?") == False
    assert is_valid("XYZ 23") == False
