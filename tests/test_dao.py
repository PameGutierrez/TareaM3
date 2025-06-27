
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
