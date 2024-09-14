# syntax=docker/dockerfile:1

# Usa a imagem(configuração) oficial do Python
FROM python:3.11

# Define o diretório de trabalho
WORKDIR /MyApp

# Copia o arquivo requirements e instala
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copia todo o codigo
COPY . .

# Define o comando para executar 
CMD ["flask", "run", "--host=0.0.0.0"]