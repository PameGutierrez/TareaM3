
from typing import List
from crud_tdd.models import Item
from crud_tdd.dao    import ItemDao

class ItemService:
    def __init__(self, dao: ItemDao):
        self._dao = dao

    def crear_item(self, item: Item) -> Item:
        if not item.nombre:
            raise ValueError("El nombre no puede estar vacío")
        self._dao.create(item)
        return item

    def obtener_todos(self) -> List[Item]:
        return self._dao.read_all()

    def actualizar_item(self, item: Item) -> None:
        ids = [i.id for i in self._dao.read_all()]
        if item.id not in ids:
            raise ValueError(f"Item con id={item.id} no existe")
        self._dao.update(item)

    def borrar_item(self, id: int) -> None:
        self._dao.delete(id)
