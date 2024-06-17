from plates import is_valid

def test_valid_plates():
    assert is_valid("CS50") == True

def test_cero_first():
    assert is_valid("CS05") == False

def test_numbers_midle():
    assert is_valid("CP50P") == False

def test_no_punctuation_spaces():
    assert is_valid("CS.50") == False
    assert is_valid("CS 50") == False

def test_corrct_lenght():
    assert is_valid("A2") == False
    assert is_valid("AAAA2222") == False
