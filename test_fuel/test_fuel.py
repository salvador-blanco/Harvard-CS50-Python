from fuel import gauge
from fuel import convert
import pytest

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(75) == "75%"

def test_convert():
    assert convert("3/4") == 75

def test_no_numeric():
    with pytest.raises(ValueError):
        convert("a/4")
    with pytest.raises(ValueError):
        convert("2/1")

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
