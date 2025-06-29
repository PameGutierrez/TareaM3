# src/crud_tdd/dao.py

import sqlite3
import os
from typing import List
from crud_tdd.models import Item
from crud_tdd.db import DB_PATH

# ——————————————————————————————
# 1) DAO en memoria (para tests de unidad)
# ——————————————————————————————

class ItemDao:
    def create(self, item: Item) -> None:
        raise NotImplementedError
    def read_all(self) -> List[Item]:
        raise NotImplementedError
    def update(self, item: Item) -> None:
        raise NotImplementedError
    def delete(self, id: int) -> None:
        raise NotImplementedError

class ItemDaoImpl(ItemDao):
    def __init__(self):
        self._almacen: List[Item] = []

    def create(self, item: Item) -> None:
        self._almacen.append(item)

    def read_all(self) -> List[Item]:
        return list(self._almacen)

    def update(self, item: Item) -> None:
        for i, e in enumerate(self._almacen):
            if e.id == item.id:
                self._almacen[i] = item
                return
        raise ValueError("Item no encontrado")

    def delete(self, id: int) -> None:
        self._almacen = [e for e in self._almacen if e.id != id]


# ——————————————————————————————
# 2) DAO sobre SQLite (para tests de integración)
# ——————————————————————————————

class ItemDaoSqlImpl:
    def _connect(self):
        return sqlite3.connect(DB_PATH)

    def create(self, item: Item) -> None:
        conn = self._connect()
        cur  = conn.cursor()
        cur.execute("INSERT INTO items(nombre) VALUES(?)", (item.nombre,))
        conn.commit(); conn.close()

    def read_all(self) -> List[Item]:
        conn = self._connect()
        cur  = conn.cursor()
        cur.execute("SELECT id, nombre FROM items")
        rows = cur.fetchall()
        conn.close()
        return [Item(id=r[0], nombre=r[1]) for r in rows]

    def update(self, item: Item) -> None:
        conn = self._connect()
        cur  = conn.cursor()
        cur.execute("UPDATE items SET nombre = ? WHERE id = ?", (item.nombre, item.id))
        if cur.rowcount == 0:
            raise ValueError("Item no encontrado")
        conn.commit(); conn.close()

    def delete(self, id: int) -> None:
        conn = self._connect()
        cur  = conn.cursor()
        cur.execute("DELETE FROM items WHERE id = ?", (id,))
        conn.commit(); conn.close()
