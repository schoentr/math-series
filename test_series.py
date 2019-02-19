from series import fibonacci, lucas, sum_series
# ********* fibonacci ********
def test_third_index():
    actual = fibonacci(3)
    expected = 1
    assert expected == actual

def test_fourth_index():
    actual = fibonacci(4)
    expected = 2
    assert expected == actual
def test_fifth_index():
    actual = fibonacci(5)
    expected = 3
    assert expected == actual
def test_sixth_index():
    actual = fibonacci(6)
    expected = 5
    assert expected == actual

#  ******  lucas testing   ********
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

# *******  sum testing ***********
def test_sum_fifth_index():
    actual = sum_series(5 , 0, 1)
    expected = 3
    assert expected == actual
def test_sum_two_index():
    actual = sum_series(5, 2, 1)
    expected = 7
    assert expected == actual
def test_sum_x_index():
    actual = sum_series(6, 2, 1)
    expected = 11
    assert expected == actual
