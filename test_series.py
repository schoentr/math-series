from series import  fibSeq, lucas

def test_third_index():
    actual = fibSeq(3)
    expected = 1
    assert expected == actual

def test_fourth_index():
    actual = fibSeq(4)
    expected = 2
    assert expected == actual
def test_fifth_index():
    actual = fibSeq(5)
    expected = 3
    assert expected == actual
def test_sixth_index():
    actual = fibSeq(6)
    expected = 5
    assert expected == actual
def test_lucas_third_index():
    actual = lucas(3)
    expected = 3
    assert expected == actual
def test_lucas_forth_index():
    actual = lucas(4)
    expected = 4
    assert expected == actual
def test_lucas_fifth_index():
    actual = lucas(5)
    expected = 7
    assert expected == actual