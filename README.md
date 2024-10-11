# Gestão API

## Acesse
- http://localhost:8000

Api para registro de tarefas e horas trabalhadas

## Sobre o sistema
- Usuários: podem ser vinculados como responsável nas tarefas.
- Tarefas: tem a ideia de uma solicitação, para ser executada.
- Atividades: Tem o objetivo de registrar as horas trabalhadas de cada usuário em cima de uma tarefa.

## Requisitos
- Python 3.13
- Poetry 1.8.3

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

## Uso via Docker
```bash
# Iniciar api
docker compose up
```

## Banco de dados
É usado o sqlite

![Estrutura do banco](docs/estrutura_banco.png)
