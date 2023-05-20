from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = '49958cabc486038474ddf21ec53e9358'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///api_hashtag.db'

database = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Para acessar a página, realize login'
login_manager.login_message_category = 'alert alert-warning'

token_cadastro = 'uhdfaAADF123'

from api_hashtag import routes