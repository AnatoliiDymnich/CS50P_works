from seasons import check_date
import pytest


def test_input_date():
    assert check_date("1999-01-01") == [1999, 1, 1]
    assert check_date("2020-10-30") == [2020, 10, 30]


def test_wrong_input_date():
    with pytest.raises(SystemExit):
        check_date("this is date")
    with pytest.raises(SystemExit):
        check_date("01, 01, 1999")
    with pytest.raises(SystemExit):
        check_date("01.01.99")
    with pytest.raises(SystemExit):
        check_date("1999-14-12")
