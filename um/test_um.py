from um import count


def test_um_inputs():
    assert count("hello, um, world") == 1
    assert count("um, hello, um, world") == 2
    assert count("um...") == 1
    assert count("Um, thanks for the album") == 1

def test_no_um_inputs():
    assert count("yum") == 0
    assert count("yummy") == 0
