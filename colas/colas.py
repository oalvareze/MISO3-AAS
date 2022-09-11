import sys
sys.path.append("..")

import uuid
from celery import Celery
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .modelos import Base, LogOperador

engine = create_engine('postgresql://miso_aas:123123123@localhost/miso_aas')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

celery_app = Celery(__name__, broker="redis://localhost:6379/0")

@celery_app.task(name='registrar_log')
def registrar_log(id, operador_id, fecha, observaciones):
    try:
        nuevo_log = LogOperador(
                id = id,
                operador_id = operador_id,
                fecha = fecha,
                observaciones = observaciones,
            )
        session.add(nuevo_log)
        session.commit()
        return True
    except:
        session.rollback()
        return False 
    
