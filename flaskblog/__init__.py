from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskblog.models import db


# create the app
app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# replace DATABASE_URI with the path to your SQLite database file
DATABASE_URI = 'sqlite:///project.db'

engine = create_engine(DATABASE_URI)

# initialize the app with the extension
db.init_app(app)

# create the database
with app.app_context():
    db.create_all()
