import pytest
from working import convert

def test_valid_values():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10:00 PM to 8:00 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 PM") == "22:30 to 20:50"

def test_invalid_values():
        with pytest.raises(ValueError):
              convert("09:00    17:00")
        with pytest.raises(ValueError):
              convert("12:60 AM to 01:00 PM")
