# src/crud_tdd/models.py

class Item:
    def __init__(self, id: int = None, nombre: str = ""): # type: ignore
        self.id = id
        self.nombre = nombre
