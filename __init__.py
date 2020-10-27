from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_minify import minify

app = Flask(__name__)

app.config["SECRET_KEY"] = "c2245399955f7be46aec6cd15da6a899"
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
minify(app=app, html=True, js=True, cssless=True)

from . import routes