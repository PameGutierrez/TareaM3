# CRUD-TDD en Python

Proyecto Python que implementa un CRUD con TDD y SQLite.

## Requisitos

- Python 3.10+
- VS Code con extensión Python
- pytest
- pytest-cov

## Instalación

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## Inicializar base de datos

```bash
python -c "from crud_tdd.db import init_db; init_db()"
