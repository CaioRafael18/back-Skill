import os
from src.helpers.logging import logger

class Config:
    # Variaveis de ambiente para configuração do banco
    USER_DB = os.getenv("USER_DB")
    PASSWORD_DB = os.getenv("PASSWORD_DB")
    DB_NAME = os.getenv("DB_NAME")
    PORT_DB = os.getenv("PORT_DB")
    MY_SECRET = os.getenv("MY_SECRET")
    DB_URL = f"postgresql+psycopg2://{USER_DB}:{PASSWORD_DB}@pgsql:5432/{DB_NAME}"
    logger.info(f'URL do banco de dados: {DB_URL}')

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = DB_URL
    JWT_SECRET_KEY = 'f3c4e5d6a7b8c9d0e1f2g3h4i5j6k7l8m9'
 