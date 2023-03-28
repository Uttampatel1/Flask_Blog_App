from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

# create the app
app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# replace DATABASE_URI with the path to your SQLite database file
DATABASE_URI = 'sqlite:///project.db'

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'uttampipaliya4@gmail.com'
app.config['MAIL_PASSWORD'] = 'ohcdwisphksqowey'

mail = Mail(app)

db = SQLAlchemy()
# initialize the app with the extension
db.init_app(app)

from flaskblog import routes
