
from typing import List
from crud_tdd.models import Item
from crud_tdd.db import ConnectionFactory

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
    """
    Implementación en memoria de la interfaz ItemDao.
    """
    def __init__(self):
        self._almacen: List[Item] = []

    def create(self, item: Item) -> None:
        self._almacen.append(item)

    def read_all(self) -> List[Item]:
        return list(self._almacen)

    def update(self, item: Item) -> None:
        for idx, existente in enumerate(self._almacen):
            if existente.id == item.id:
                self._almacen[idx] = item
                return
        raise ValueError("Item no encontrado")

    def delete(self, id: int) -> None:
        self._almacen = [i for i in self._almacen if i.id != id]

class ItemDaoSqlImpl:
    """
    Implementación sobre SQLite, recibiendo la factoría de conexiones.
    """
    def __init__(self, conn_factory: ConnectionFactory):
        # conn_factory: instancia de ConnectionFactory
        self._conn_factory = conn_factory

    def _connect(self):
        # Se conecta usando la factoría inyectada
        return self._conn_factory.get_connection()

    def create(self, item: Item) -> None:
        conn = self._connect()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO items(nombre) VALUES(?)",
            (item.nombre,)
        )
        conn.commit()
        conn.close()

    def read_all(self) -> List[Item]:
        conn = self._connect()
        cur = conn.cursor()
        cur.execute("SELECT id, nombre FROM items")
        rows = cur.fetchall()
        conn.close()
        return [Item(id=row[0], nombre=row[1]) for row in rows]

    def update(self, item: Item) -> None:
        conn = self._connect()
        cur = conn.cursor()
        cur.execute(
            "UPDATE items SET nombre = ? WHERE id = ?",
            (item.nombre, item.id)
        )
        if cur.rowcount == 0:
            conn.close()
            raise ValueError("Item no encontrado")
        conn.commit()
        conn.close()

    def delete(self, id: int) -> None:
        conn = self._connect()
        cur = conn.cursor()
        cur.execute("DELETE FROM items WHERE id = ?", (id,))
        conn.commit()
        conn.close()

