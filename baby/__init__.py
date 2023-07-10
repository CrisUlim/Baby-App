from flask import Flask
import secrets



app = Flask(__name__)
app.static_folder = 'static'
secret_key = secrets.token_hex(16)
app.config['SECRET_KEY'] = secret_key


from baby import routes