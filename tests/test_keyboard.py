import pytest

from src.keyboard import Keyboard


def test_keyboard_attributes():
    k = Keyboard("Test Keyboard", 50, 10)
    assert k.name == "Test Keyboard"
    assert k.price == 50
    assert k.quantity == 10
    assert k.language == "EN"


def test_keyboard_change_lang():
    k = Keyboard("Test Keyboard", 50, 10, "EN")
    k.change_lang()
    assert k.language == "RU"
    k.change_lang()
    assert k.language == "EN"


def test_keyboard_str():
    k = Keyboard("Test Keyboard", 50, 10, "EN")
    assert str(k) == "Test Keyboard"


def test_keyboard_invalid_language():
    with pytest.raises(AttributeError):
        k = Keyboard("Test Keyboard", 50, 10)
        k.language = 'CH'
