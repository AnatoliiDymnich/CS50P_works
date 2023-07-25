

from twttr import shorten
import pytest


def test_shorten_lower():
    assert shorten("this is cs50") == "ths s cs50"


def test_shorten_upper():
    assert shorten("TWITTER") == "TWTTR"


def test_punctuation():
    assert shorten("!?,.") == "!?,."


def test_shorten_with_assert_error():
    with pytest.raises(AssertionError):
        assert shorten("My name is") == "m nm s"
