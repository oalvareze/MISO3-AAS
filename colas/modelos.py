from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.ext.declarative import declarative_base                                                                                         
from sqlalchemy import Column, Float, Integer, String, DateTime

Base = declarative_base()

class LogOperador(Base):
    __tablename__ = 'log_operador'
    id = Column(UUID(as_uuid=True), primary_key=True)
    operador_id = Column(UUID(as_uuid=True))
    fecha = Column(DateTime)
    observaciones = Column(String(2048))
    