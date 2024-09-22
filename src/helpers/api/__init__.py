from flask import Blueprint
from flask_restful import Api

from src.resources.indexResource import IndexResource
from src.resources.userResource import UserRegisterResource, UsersResource
from src.resources.administradorResource import listAdministradores
from src.resources.professorResource import listProfessores

# Cria um blueprint para a API com prefixo "/api"
blueprint = Blueprint('api', __name__)
api = Api(blueprint, prefix="/api")

# Definindo as rotas da api
api.add_resource(IndexResource, '/')
api.add_resource(UserRegisterResource, '/register')
api.add_resource(UsersResource, '/users')
api.add_resource(listProfessores, '/professores')
api.add_resource(listAdministradores, '/administradores')
