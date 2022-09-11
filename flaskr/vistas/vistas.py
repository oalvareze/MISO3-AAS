from flask_restful import Resource
from ..modelos import db, LogOperador, LogOperadorSchema
from flask import request

log_operador_schema = LogOperadorSchema()

class VistaLogOperadores(Resource):
    
    def post(self):
        nuevo_log = LogOperador(
            id = request.json['id'],
            operador_id = request.json['operador_id'],
            fecha = request.json['fecha'],
            observaciones = request.json['observaciones'],
        )
        
        db.session.add(nuevo_log)
        db.session.commit()
        return log_operador_schema.dump(nuevo_log)
        
    
    