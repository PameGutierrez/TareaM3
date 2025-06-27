
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
