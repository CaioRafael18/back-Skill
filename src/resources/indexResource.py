from flask_restful import Resource

class IndexResource(Resource):
    def get(self):
        return {'method': 'get', 'versao': '0.1', 'message': 'Olá, conexão realizada'}

    def post(self):
        return {'method': 'post', 'versao': '0.1', 'message': 'Olá, conexão realizada'}

    def put(self):
        return {'method': 'put', 'versao': '0.1', 'message': 'Olá, conexão realizada'}

    def delete(self):
        return {'method': 'delete', 'versao': '0.1', 'message': 'Olá, conexão realizada'}
