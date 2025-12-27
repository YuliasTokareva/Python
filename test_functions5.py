import pytest

from functions5 import count_glasn

def test_empty_string():
    assert count_glasn("") == 0

def test_only_soglasn():
    assert count_glasn("bcdfg") == 0

def test_only_glasn_english():
    assert count_glasn("aeiouy") == 6

def test_only_glasn_russian():
    assert count_glasn("аеёиоуыэюя") == 10

def test_mixed_text():
    assert count_glasn("Hello, мир!") == 3

def test_upper_text():
    assert count_glasn("HELLO") == 2

def test_not_bukva():
    assert count_glasn("1, 2, 4") == 0

def test_none_input():
    with pytest.raises(TypeError):
        count_glasn(None)

def test_non_string_input():
    with pytest.raises(TypeError):
        count_glasn(123)

