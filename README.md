# CRUD-TDD en Python

Proyecto de ejemplo que implementa un CRUD con enfoque TDD y SQLite.

## Requisitos

* Python 3.10+
* VS Code (o tu editor favorito) con extensión de Python
* `pytest` para pruebas unitarias
* `pytest-cov` para cobertura de código

## Clonar el repositorio

```bash
git clone https://github.com/PameGutierrez/TareaM3.git
cd TareaM3
```

## Instalación

1. **Crea y activa un entorno virtual**:

   ```bash
   python -m venv venv
   # Windows PowerShell:
   .\venv\Scripts\Activate.ps1
   # Windows CMD:
   .\venv\Scripts\activate.bat
   # macOS/Linux:
   source venv/bin/activate
   ```
2. **Instala dependencias**:

   ```bash
   pip install -r requirements.txt
   ```
3. **Inicializa la base de datos**:

   ```bash
   python -c "from crud_tdd.db import init_db; init_db()"
   ```

## Estructura del proyecto

```
TareaM3/
├── README.md
├── main.py             # Demo de CRUD vía ItemService
├── requirements.txt
├── pytest.ini          # Configuración pytest (ruta src/)
├── .github/
│   └── workflows/      # GitHub Actions CI (pytest, cobertura)
├── htmlcov/            # Reporte HTML de cobertura
├── src/
│   └── crud_tdd/
│       ├── models.py   # Modelo Item
│       ├── dao.py      # DAO en memoria + SQL (factoría)
│       ├── db.py       # init_db() y ConnectionFactory
│       └── service.py  # Lógica de negocio (ItemService)
└── tests/
    └── test_dao.py    # Tests unitarios e integración SQL
```

## Ejecutar la demo

Puedes ver un flujo completo de creación, lectura, actualización y borrado ejecutando:

```bash
python main.py
```

## Ejecutar las pruebas

```bash
pytest -q
```

## Cobertura de tests

Mide la cobertura y genera un reporte HTML:

```bash
pytest --cov=crud_tdd --cov-report html -q
```

Luego abre en tu navegador:

```
htmlcov/index.html
```

y verifica que la cobertura global sea ≥ 80 %.

## Integración continua (GitHub Actions)

Se incluye un workflow en `.github/workflows/python-ci.yml` que:

1. Ejecuta pytest en cada push/pull\_request a `main`.
2. Genera un reporte de cobertura.

Puedes ver el estado en la pestaña **Actions** de tu repositorio.

## Buenas prácticas aplicadas

* **TDD**: El historial de commits sigue el ciclo Red-Green-Refactor.
* **SRP**: `ItemService` gestiona reglas de negocio; `dao.py` se encarga solo de persistencia.
* **DIP**: `ItemDaoSqlImpl` recibe la `ConnectionFactory`, evitando dependencias directas a SQLite.
* **DRY/KISS**: Código modular y legible, sin duplicaciones.

---


