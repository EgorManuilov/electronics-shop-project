"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from pytest import fixture

from src.item import Item


@fixture
def item():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 200000


def test_apply_discount(item):
    item.apply_discount()
    assert item.price == 10000.0


def test_get_name(item):
    assert item.name == "Смартфон"


def test_set_name(item):
    item.name = "test"
    assert item.name == "test"


def test_not_valid_name(item):
    with pytest.raises(ValueError):
        item.name = 'болеедесятибукв'


def test_instantiate_from_csv(item):
    item.instantiate_from_csv()
    assert len(item.all) == 5


def test_string_to_number(item):
    assert item.string_to_number('666') == 666


def test_not_valid_string(item):
    assert item.string_to_number('один') == "Невозможно преобразовать в число"


def test_repr(item):
    assert repr(item) == "Item('Смартфон', 10000, 20)"


def test_str(item):
    assert str(item) == "Смартфон"


def test_instantiate_from_csv_error():
    Item.CSV_PATH = "error_path"
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv()


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    item = Item.all[1]
    assert item.name == "Ноутбук"
    assert item.price == "1000"
    assert item.quantity == "3"

