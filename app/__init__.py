from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
import os

#local imports
from config import app_config

#db variable initialization
db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config['development'])
    db.init_app(app)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    migrate = Migrate(app, db)
    Bootstrap(app)
    from app.models import models
    login_manager.init_app(app)
    login_manager.login_message = 'You must be logged in to access this page.'
    login_manager.login_view = 'auth.login'
    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    from app.job import job as job_blueprint
    app.register_blueprint(job_blueprint)

    
    return app