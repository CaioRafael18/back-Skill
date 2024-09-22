from flask_restful import Resource
from src.models.Administrador import Administrador

class listAdministradores(Resource):
    def get(self):
        try:
            administradores = Administrador.query.all() 
            administradores_list = [
                {
                    "id": administrador.id,
                    "user_id": administrador.user_id,
                    "matricula": administrador.matricula,
                    "name": administrador.user.name,
                    "email": administrador.user.email
                }
                for administrador in administradores
            ]
            return {"administradores": administradores_list}, 200
        except Exception as e:
            return {"mensagem": "Erro ao exibir a lista de administradores!", "erro": str(e)}, 500
        