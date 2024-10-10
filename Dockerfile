# Usa uma imagem base do Python
FROM python:3.13-slim

ENV PYTHONUNBUFFERED 1

# Instala as dependências Python
RUN pip install --no-cache-dir poetry

# Configura o diretório de trabalho
WORKDIR /app

# Copia todo o conteúdo do projeto
COPY . .

# Instala as dependências do projeto
RUN poetry install --no-root

# Criar banco de dados
RUN poetry run python manage.py migrate

EXPOSE 8000

# Inicia api
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
