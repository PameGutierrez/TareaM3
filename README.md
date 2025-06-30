# CRUD-TDD en Python

Proyecto de ejemplo que implementa un CRUD con enfoque TDD y SQLite.

## Requisitos

* Python 3.10+
* pytest
* pytest-cov

## Clonar el repositorio

```bash
git clone https://github.com/PameGutierrez/TareaM3.git
cd TareaM3
```

## Instalación

1. Crea y activa un entorno virtual:

   ```bash
   python -m venv venv
   # Windows PowerShell
   .\venv\Scripts\Activate.ps1
   # macOS/Linux
   source venv/bin/activate
   ```
2. Instala dependencias:

   ```bash
   pip install -r requirements.txt
   ```
3. Inicializa la base de datos:

   ```bash
   python -c "from crud_tdd.db import init_db; init_db()"
   ```

## Estructura del proyecto

```
TareaM3/
├── README.md
├── main.py
├── requirements.txt
├── pytest.ini
├── htmlcov/          # Reporte HTML de cobertura
├── src/
│   └── crud_tdd/
│       ├── models.py # Modelo Item
│       ├── dao.py    # DAO en memoria + SQL (factoría)
│       ├── db.py     # init_db() y ConnectionFactory
│       └── service.py# Lógica de negocio (ItemService)
└── tests/
    └── test_dao.py  # Tests unitarios e integración SQL
```

## Ejecutar las pruebas

```bash
pytest -q
```

## Cobertura de tests

```bash
pytest --cov=crud_tdd --cov-report html -q
```

Luego abre en tu navegador:

```
htmlcov/index.html
```

y verifica que la cobertura global sea ≥ 80 %.
