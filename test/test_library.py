from library.my_library import square


def test_square_2_equals_4():
    assert square(2) == 4


# execute using  $env:PYTHONPATH="."; pytest