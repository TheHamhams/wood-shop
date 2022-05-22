import os 
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager 

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

bcrypt = Bcrypt(app)

from wood_shop import routes