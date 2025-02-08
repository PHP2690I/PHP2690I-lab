import pytest

from lab4.Demo_pytest.add_function import add

def test_add_positive_numbers():
    assert add(1, 2) == 3


def test_add_negative_numbers():
    assert add(-1, -2) == -3


def test_add_mixed_numbers():
    assert add(1, -2) == -1
    assert add(-1, 2) == 1


def test_bad_input():
    with pytest.raises(TypeError):
        add('a', 1)
    with pytest.raises(TypeError):
        add(1, 'a')
    with pytest.raises(TypeError):
        add('a', 'b')

# Run the test
if __name__ == '__main__':
    pytest.main(['-s', 'add_func_test.py'])