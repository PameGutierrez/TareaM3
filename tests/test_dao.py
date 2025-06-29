
import pytest
from crud_tdd.dao import ItemDao, ItemDaoImpl  
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

from crud_tdd.db import init_db
from crud_tdd.dao import ItemDaoSqlImpl
from crud_tdd.models import Item

class TestItemDaoSql:
    def setup_method(self):
        init_db()
        self.dao = ItemDaoSqlImpl()

    def test_create_y_read_all_sql(self):
        self.dao.create(Item(nombre="JDBC"))
        lista = self.dao.read_all()
        assert any(i.nombre == "JDBC" for i in lista)

    def test_update_sql(self):
        self.dao.create(Item(nombre="Antes"))
        item = self.dao.read_all()[0]
        item.nombre = "Después"
        self.dao.update(item)
        assert self.dao.read_all()[0].nombre == "Después"

    def test_delete_sql(self):
        self.dao.create(Item(nombre="X"))
        id_ = self.dao.read_all()[0].id
        self.dao.delete(id_)
        assert self.dao.read_all() == []
