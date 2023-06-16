from src.phone import Phone
import pytest

@pytest.fixture
def phone1():
    return Phone('IPhone 14', 120000, 5, 2)


def test_str_method(phone1):
    assert str(phone1) == 'IPhone 14'

def test_repr_method(phone1):
    assert repr(phone1) == "Phone('IPhone 14', 120000, 5, 2)"


