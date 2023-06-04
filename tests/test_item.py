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
