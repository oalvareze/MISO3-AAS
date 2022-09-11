from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
import uuid

db = SQLAlchemy()

class LogOperador(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    operador_id = db.Column(UUID(as_uuid=True))
    fecha = db.Column(db.DateTime)
    observaciones = db.Column(db.String(2048))
    
    def __repr__(self) -> str:
        return "{}, {}, {} : {}".format(self.id, self.operador_id, self.fecha, self.observaciones)
    
class LogOperadorSchema(SQLAlchemyAutoSchema):
    class Meta:
         model = LogOperador
         include_relationships = True
         load_instance = True