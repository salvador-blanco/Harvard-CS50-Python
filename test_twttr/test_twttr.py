from twttr import shorten

def test_shorten_upercase():
    assert shorten("I LIKE CATS") == " LK CTS"
    assert shorten("I HATE DOGS") == " HT DGS"

def test_numbers():
    assert shorten("1234 1234") == "1234 1234"
    assert shorten("432 432") == "432 432"

def test_no_consonants():
    assert shorten("aeiou aeiou") == " "
    assert shorten("uoiea uoiea") == " "

def test_omitting_punctuation():
    assert shorten("A.Alice 1234") == ".lc 1234"
    assert shorten("What's your name?") == "Wht's yr nm?"
