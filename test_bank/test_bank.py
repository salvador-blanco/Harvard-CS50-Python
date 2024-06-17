from bank import value

def test_bank_hello():
    assert value("Hello") == 0
    assert value("Hello, Newman") == 0

def test_bank_h():
    assert value("How you doing?") == 20

def test_bank_no_h():
    assert value("What's happening?") == 100
