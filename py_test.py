import pytest
from app import add, is_even, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_is_even():
    assert is_even(4) == True
    assert is_even(5) == False

def test_divide():
    assert divide(10, 2) == 5.0

def test_divide_by_zero():
    with pytest.raises(ValueError, match="На ноль делить нельзя!"):
        divide(10, 0)