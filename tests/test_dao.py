
import pytest
from crud_tdd.dao import ItemDao
from crud_tdd.models import Item

class DummyDao(ItemDao):
    pass

def test_create_no_implementado():
    dao = DummyDao()
    with pytest.raises(NotImplementedError):
        dao.create(Item(1, "X"))

def test_read_all_no_implementado():
    dao = DummyDao()
    with pytest.raises(NotImplementedError):
        dao.read_all()

def test_update_no_implementado():
    dao = DummyDao()
    with pytest.raises(NotImplementedError):
        dao.update(Item(1, "X"))

def test_delete_no_implementado():
    dao = DummyDao()
    with pytest.raises(NotImplementedError):
        dao.delete(1)

def test_create_y_read_all():
    dao = ItemDaoImpl()
    dao.create(Item(1, "A"))
    assert any(i.nombre == "A" for i in dao.read_all())

def test_update_exitoso():
    dao = ItemDaoImpl()
    dao.create(Item(1, "Antes"))
    dao.update(Item(1, "Después"))
    assert dao.read_all()[0].nombre == "Después"

def test_delete_exitoso():
    dao = ItemDaoImpl()
    dao.create(Item(1, "X"))
    dao.delete(1)
    assert dao.read_all() == []
