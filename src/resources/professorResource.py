from flask_restful import Resource
from src.models.Professor import Professor

class listProfessores(Resource):
    def get(self):
        try:
            professores = Professor.query.all() 
            professores_list = [
                {
                    "id": professor.id,
                    "user_id": professor.user_id,
                    "matricula": professor.user.matricula,
                    "name": professor.user.name,
                    "email": professor.user.email
                }
                for professor in professores
            ]
            return {"professores": professores_list}, 200
        except Exception as e:
            return {"mensagem": "Erro ao exibir a lista de professores!", "erro": str(e)}, 500


