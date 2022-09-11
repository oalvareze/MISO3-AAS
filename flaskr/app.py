from datetime import datetime
from uuid import UUID
from flaskr import create_app
from flask_restful import Api

from flaskr.vistas.vistas import VistaLogOperadores
from .modelos import db, LogOperador, LogOperadorSchema
from sqlalchemy.sql import func

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(VistaLogOperadores, '/log_operadores')