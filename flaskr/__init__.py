from flask import Flask

def create_app(config_name):
    app= Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://miso_aas:123123123@localhost/miso_aas'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app

