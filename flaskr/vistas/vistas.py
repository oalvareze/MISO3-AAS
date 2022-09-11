from flask_restful import Resource
from flask import request
from celery import Celery

celery_app = Celery(__name__, broker="redis://localhost:6379/0")

@celery_app.task(name='registrar_log')
def registrar_log(*arg):
    pass
class VistaLogOperadores(Resource):
    
    def post(self):
        argumentos = (request.json["id"],request.json["operador_id"],request.json["fecha"],request.json["observaciones"])
        registrar_log.apply_async(argumentos, queue='logs')
        
    
    