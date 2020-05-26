from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
# app.config.from_object('config.DevelopementConfig')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app, resources={r'/*': {'origins': '*'}})
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:OTESKone2020@localhost:5433/flask_vue_app_db'
app.config['SECRET_KEY'] = 'A realy long long long very-very secret key'

from . import views
