from flask_restful import Resource
from src.models.Aluno import Aluno

class listAlunos(Resource):
    def get(self):
        try:
            alunos = Aluno.query.all() 
            alunos_list = [
                {
                    "id": aluno.id,
                    "user_id": aluno.user_id,
                    "matricula": aluno.user.matricula,
                    "name": aluno.user.name,
                    "email": aluno.user.email
                }
                for aluno in alunos
            ]
            return {"alunos": alunos_list}, 200
        except Exception as e:
            return {"mensagem": "Erro ao exibir a lista de alunos!", "erro": str(e)}, 500


