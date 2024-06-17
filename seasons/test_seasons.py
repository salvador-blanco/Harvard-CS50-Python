from datetime import date
from seasons import DateInMinutes
import pytest

today_year = date.today().year
today_month = date.today().month
today_day = date.today().day

def test_one_year_from_now():
    assert DateInMinutes(today_year-1,today_month,today_day + 1).get_str() == "Five hundred twenty-five thousand, six hundred minutes"

def test_invalid_input():
    with pytest.raises(ValueError):
        DateInMinutes(str(today_year-1),str(today_month),str(today_day)).get_str()
