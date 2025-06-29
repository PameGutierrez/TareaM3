
from crud_tdd.db      import init_db, ConnectionFactory
from crud_tdd.dao     import ItemDaoSqlImpl
from crud_tdd.service import ItemService
from crud_tdd.models  import Item

def run_demo():
    # 1) (Re)crea la BD limpia
    init_db()

    # 2) Monta la factoría y el DAO SQL
    conn_fac = ConnectionFactory()
    dao_sql  = ItemDaoSqlImpl(conn_fac)

    # 3) Crea el servicio inyectando el DAO
    service = ItemService(dao_sql)

    # 4) Usa el servicio para las operaciones
    print("Creando un item...")
    item1 = service.crear_item(Item(nombre="Prueba"))
    print("Listado tras create:", service.obtener_todos())

    print("Actualizando el item...")
    item1.nombre = "Prueba Modificada"
    service.actualizar_item(item1)
    print("Listado tras update:", service.obtener_todos())

    print("Borrando el item...")
    service.borrar_item(item1.id)
    print("Listado tras delete:", service.obtener_todos())

if __name__ == "__main__":
    run_demo()
