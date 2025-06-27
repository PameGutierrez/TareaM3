
import pytest
from crud_tdd.models import Item

def test_constructor_por_defecto():
    item = Item()
    assert item is not None

def test_constructor_con_parametros():
    item = Item(1, "Prueba")
    assert item.id == 1
    assert item.nombre == "Prueba"

def test_setters_y_getters():
    item = Item()
    item.id = 2
    item.nombre = "Otro"
    assert item.id == 2
    assert item.nombre == "Otro"
