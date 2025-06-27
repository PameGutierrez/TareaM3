# src/crud_tdd/dao.py

from crud_tdd.models import Item
from typing import List

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
        for idx, existente in enumerate(self._almacen):
            if existente.id == item.id:
                self._almacen[idx] = item
                return
        raise ValueError("Item no encontrado")

    def delete(self, id: int) -> None:
        self._almacen = [i for i in self._almacen if i.id != id]

