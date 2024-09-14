from flask import Blueprint, request, jsonify
from src.models.Usuario import Usuario
from app import db
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

usuario_bp = Blueprint('usuario', __name__)

@usuario_bp.route('/cadastrar', methods=['POST'])
def cadastrar():
    data = request.get_json()
    print("Dados recebidos:", data)
    name = data.get('name')
    username = data.get('username')
    email = data.get('email')
    phone_number = data.get('phone_number')
    password = data.get('password')
    
    print("Senha recebida:", password)
    passwordHash = generate_password_hash(password, method='pbkdf2:sha256')
    print("Senha hash:", passwordHash)
    
    novoUsuario = Usuario(name=name, username=username, email=email, phone_number=phone_number, password=passwordHash)
    
    try:
        db.session.add(novoUsuario)
        db.session.commit()
    except Exception as e:
        print("Erro ao adicionar usuário:", e)
        db.session.rollback()
        return jsonify({"mensagem": "Erro ao cadastrar usuário!"}), 500
    
    return jsonify({"mensagem": "Usuário Cadastrado!"}), 201

@usuario_bp.route('/logar', methods=['POST'])
def logar():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    usuario = Usuario.query.filter_by(username=username).first()
    
    if usuario:
        if check_password_hash(usuario.password, password):
            tokenDeAcesso = create_access_token(identity=usuario.id)
            return jsonify(tokenDeAcesso=tokenDeAcesso), 200
        else:
            return jsonify({"mensagem": "Senha ou Nome de Usuário incorreto!"}), 401
    else:
        return jsonify({"mensagem": "Usuário não encontrado!"}), 401

@usuario_bp.route("/", methods=["GET"])
def hello():
    return "Olá, conexao realizada"