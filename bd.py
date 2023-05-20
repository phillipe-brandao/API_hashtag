from api_hashtag import app, database, bcrypt
from api_hashtag.models import Usuario, Requisicao
from datetime import datetime

'''Criar o banco de dados'''
with app.app_context():
    database.drop_all()
    database.create_all()
    usuario = Usuario(email='admin@gmail.com', senha=bcrypt.generate_password_hash('123456'))
    database.session.add(usuario)
    database.session.commit()

