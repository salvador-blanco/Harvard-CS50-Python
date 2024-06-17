from numb3rs import validate

def test_valid_IP():
    assert validate("1.2.3.4") == True
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.0") == True

def test_invalid_IP():
    assert validate("275.3.6.28") == False
    assert validate("2.275.6.28") == False
    assert validate("27.3.275.28") == False
    assert validate("25.3.6.275") == False
    assert validate("cat") == False

