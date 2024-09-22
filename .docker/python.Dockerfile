# syntax=docker/dockerfile:1

# Usa a imagem(configuração) oficial do Python
FROM python:3.11

# Instalar o cliente PostgreSQL
RUN apt-get update && apt-get install -y postgresql-client

# Define o diretório de trabalho
RUN mkdir /app
WORKDIR /app
COPY . /app

# Declarar variáveis de ambiente.
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_DEBUG=true
ENV FLASK_ENV=development

# Instalar as dependências.
RUN pip install --no-cache-dir -r requirements.txt

# Porta de acesso.
EXPOSE 5000

# running Flask as a module
CMD ["flask", "run"]