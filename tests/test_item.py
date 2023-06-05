"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

item1 = Item("Смартфон", 20000, 10)

def test_calculate_total_price():
    assert item1.calculate_total_price() == 200000

def test_pay_rate():
    assert Item.pay_rate == 1

def test_apply_discount():
    Item.pay_rate = 1.5
    item1.apply_discount()
    assert item1.price == 30000

def test_string_to_number():
    assert Item.string_to_number('1') == 1
    assert Item.string_to_number('1.2') == 1

def test_name():
    item1.name = 'Телефон'
    assert item1.name == 'Телефон'
    with pytest.raises(Exception):
        item1.name = 'Суперсмартфон'


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    with pytest.raises(Exception):
        assert len(Item.all) == 0


