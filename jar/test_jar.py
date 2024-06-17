import jar
import pytest

def test_initial_values():
    chaba_jar = jar.Jar(5)
    assert chaba_jar.size == 0
    assert chaba_jar.capacity == 5

def test_exceding_capasity():
    with pytest.raises(ValueError):
        chaba_jar = jar.Jar(5)
        chaba_jar.deposit(6)

def test_exceding_capasity():
    with pytest.raises(ValueError):
        chaba_jar = jar.Jar(5)
        chaba_jar.withdraw(6)

def test_str():
    chaba_jar = jar.Jar(5)
    assert str(chaba_jar) == ''
    chaba_jar.deposit(2)
    assert str(chaba_jar) == '🍪🍪'

def test_deposit():
    chaba_jar = jar.Jar(5)
    chaba_jar.deposit(3)
    assert chaba_jar.size == 3
    chaba_jar.deposit(1)
    assert chaba_jar.size == 4

def test_withdraw():
    chaba_jar = jar.Jar(5)
    chaba_jar.deposit(5)
    chaba_jar.withdraw(3)
    assert chaba_jar.size == 2
    chaba_jar.withdraw(1)
    assert chaba_jar.size == 1








