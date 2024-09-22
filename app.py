from flask import Flask

from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

from src.helpers.config import Config
from src.helpers.database import db
from src.helpers.api import api, blueprint
from src.helpers.cors import cors
# from src.helpers.seeders import seeder

# Criar o app
app = Flask(__name__)

# Configurações
app.config.from_object(Config)

jwt = JWTManager()

# Define/inicializa o Api
api.init_app(app)

# Define/inicializa o Database
db.init_app(app)

# Inicializa o Migrate 
migrate = Migrate(app, db)

# Define/inicializa o Cors
cors.init_app(app)

# Preenche o banco
# seeder.init_app(app, db)

# Define/inicializa o JWT
jwt.init_app(app)

# Define/registra o Blueprint
app.register_blueprint(blueprint)

if __name__ == '__main__':
    app.run(debug=True)