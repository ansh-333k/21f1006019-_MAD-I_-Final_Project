from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
import os

app = Flask(__name__)

app.secret_key = 'P@ssw0rd'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.abspath(os.getcwd()) + '/database/database.sqlite3'
db = SQLAlchemy(app)

api = Api(app)

from applications.controllers import *
from applications.apis import *

if __name__ == '__main__':
    app.run(debug = True)