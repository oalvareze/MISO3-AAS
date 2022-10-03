from functools import wraps
from flask_restful import Resource
from flask import request, jsonify
from celery import Celery
from flask_jwt_extended import jwt_required, create_access_token, verify_jwt_in_request, get_jwt

from flaskr.modelos.modelos import LogOperador, LogOperadorSchema

celery_app = Celery(__name__, broker="redis://localhost:6379/0")

@celery_app.task(name='registrar_log')
def registrar_log(*arg):
    pass
def tiene_permiso(permiso):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims["permisos"] == permiso:
                return fn(*args, **kwargs)
            else:
                return {'msg':"No tiene el permiso " + permiso}, 403

        return decorator

    return wrapper


log_operador_schema = LogOperadorSchema()

class VistaLogOperadores(Resource):
    
    @tiene_permiso('agregar')
    def post(self):
        argumentos = (request.json["id"],request.json["operador_id"],request.json["fecha"],request.json["observaciones"])
        registrar_log.apply_async(argumentos, queue='logs')
        
    @tiene_permiso('leer')
    def get(self):
        return [log_operador_schema.dump(lo) for lo in LogOperador.query.all()]
        
    
    

class VistaInicioSesion(Resource):

    def post(self):
        additional_claims = {"permisos": "agregar"}
        token = create_access_token(identity=request.json["usuario"], additional_claims=additional_claims)
        return {'token': token}

