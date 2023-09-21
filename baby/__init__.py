from flask import Flask
import secrets
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.static_folder = 'static'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Baby_79762023@localhost/Login_System'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
secret_key = secrets.token_hex(16)
app.config['SECRET_KEY'] = secret_key
db = SQLAlchemy(app=app)

from baby import routes
from baby import models

