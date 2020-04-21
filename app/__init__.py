from app import views
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret_key"
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://Project1:password@localhost/Project1" # for local machine use
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://oeijnwzcwluxmu:f82857995279fc41b70869b10e3abad8edcc43aacdb41fd9c6b91c709d394508@ec2-54-147-209-121.compute-1.amazonaws.com:5432/d7seuhs2uh13ob"
# added just to suppress a warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

ALLOWED_EXTENSIONS = ['jpg', 'png', 'jpeg', 'gif', 'tiff', 'jfif']

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
app.config['UPLOAD_FOLDER'] = '/app/static/uploads'
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS
