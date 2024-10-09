# Gestão API


## Requisitos
- Python 3.13
- Poetry 1.8.2

## Uso
```bash
# Instalar as dependêcias
poetry install

# Ativar ambiente virtual
poetry shell

# Criar tabelas do banco de dados
poetry run python manage.py migrate

# Iniciar api
poetry run python manage.py runserver
```
