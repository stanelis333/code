from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/code/paskaitu_failai/Flask_web/pvz2_db/Database/users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)




