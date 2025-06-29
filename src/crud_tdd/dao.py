# src/crud_tdd/dao.py

import sqlite3
from typing import List
from crud_tdd.models import Item
from crud_tdd.db import DB_PATH

class ItemDaoSqlImpl:
    def _connect(self):
        return sqlite3.connect(DB_PATH)

    def create(self, item: Item) -> None:
        sql = "INSERT INTO items(nombre) VALUES(?)"
        conn = self._connect()
        cur = conn.cursor()
        cur.execute(sql, (item.nombre,))
        conn.commit()
        conn.close()

    def read_all(self) -> List[Item]:
        sql = "SELECT id, nombre FROM items"
        conn = self._connect()
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        conn.close()
        return [Item(id=row[0], nombre=row[1]) for row in rows]

    def update(self, item: Item) -> None:
        sql = "UPDATE items SET nombre = ? WHERE id = ?"
        conn = self._connect()
        cur = conn.cursor()
        cur.execute(sql, (item.nombre, item.id))
        if cur.rowcount == 0:
            raise ValueError("Item no encontrado")
        conn.commit()
        conn.close()

    def delete(self, id: int) -> None:
        sql = "DELETE FROM items WHERE id = ?"
        conn = self._connect()
        cur = conn.cursor()
        cur.execute(sql, (id,))
        conn.commit()
        conn.close()
