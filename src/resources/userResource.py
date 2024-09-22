from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from src.models.Administrador import Administrador
from src.models.Professor import Professor

from src.models.User import User
from src.helpers.database import db
from src.helpers.logging import logger

class UserRegisterResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', type=str, help='Nome obrigatório', required=True)
        self.parser.add_argument('matricula', type=str, help='Matricula obrigatório', required=True)
        self.parser.add_argument('email', type=str, help='Email obrigatório', required=True)
        self.parser.add_argument('password', type=str, help='Senha obrigatório', required=True)
        self.parser.add_argument('is_admin', type=bool, help='Indica se o usuário é administrador', required=True)

    def post(self):
        args = self.parser.parse_args()
        
        name = args['name']
        matricula = args['matricula']
        email = args['email']
        password = args['password']
        is_admin = args['is_admin']
        
        passwordHash = generate_password_hash(password, method='pbkdf2:sha256')
        
        newUser = User(name=name, matricula=matricula, email=email, password=passwordHash, is_admin=is_admin)
        
        try:
            db.session.add(newUser)
            db.session.commit()
            if(is_admin):
                new_administrador = Administrador(user_id=newUser.id,name=newUser.name, matricula=newUser.matricula, email=newUser.email, password=password)
                db.session.add(new_administrador)
            else:
                new_professor = Professor(user_id=newUser.id,name=newUser.name, matricula=newUser.matricula, email=newUser.email, password=password)
                db.session.add(new_professor)
            db.session.commit()
            
            return {"mensagem": "Usuário Cadastrado!"}, 201
        except Exception as e:
            logger.ERROR(f'Erro ao cadastrar novo usuário: {e}')
            db.session.rollback()
            return {"mensagem": "Erro ao cadastrar usuário!"}, 500
        

class UsersResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('email', type=str, help='Email obrigatório', required=True)
        self.parser.add_argument('password', type=str, help='Senha obrigatório', required=True)

    def get(self):
        try:
            users = User.query.all()  
            users_list = [
                {"id": user.id, "name": user.name, "matricula": user.matricula, "email": user.email}
                for user in users
            ]
            return {"usuarios": users_list}, 200
        except Exception as e:
            return {"mensagem": "Erro ao exibir a lista de usuários!", "erro": str(e)}, 500

    def post(self):
        args = self.parser.parse_args()
        email = args['email']
        password = args['password']
        
        user = User.query.filter_by(email=email).first()
        
        if user:
            if check_password_hash(user.password, password):
                access_token = create_access_token(identity=user.id)
                return {"access_token": access_token}, 200
            else:
                return {"mensagem": "Senha ou Nome de Usuário incorreto!"}, 401
        else:
            return {"mensagem": "Usuário não encontrado!"}, 401
