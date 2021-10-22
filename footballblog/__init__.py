import os
from enum import unique
import re
from footballblog.config import Config
from flask import Flask, app, render_template, flash, url_for, redirect
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from flask import redirect
# from forms import RegistrationForm, Loginform
from datetime import datetime
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_manager
from flask_mail import Mail



db = SQLAlchemy()
bcrypt=Bcrypt()
login_manager=LoginManager()
login_manager.login_view ='users.login'
login_manager.login_message_category='info'

mail = Mail()






def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)


    from footballblog.users.routes import users
    from footballblog.posts.routes import posts
    from footballblog.main.routes import main
    from footballblog.errors.handlers import errors
   

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
    

