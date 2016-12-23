#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    backend package
    ~~~~~~~~~~~~~~~

    This is the main module of this application.

    Flask extensions included in this application:
    - Flask-Bcrypt     : Used for hashing passwords.
    - Flask-SQLAlchemy : Used for creating database models (using SQLAlchemy).
    - Flask-Restless   : Used for easy RESTful API generation.
    - Flask-Script     : Used for adding support for command-line tasks.
    - Flask-Migrate    : Used for performing SQLAlchemy database migrations.
"""

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager
from flask_script import Manager
from flask_migrate import Migrate


# Creating the Flask app
app = Flask(__name__,
            template_folder='../frontend',
            static_url_path='',
            static_folder='../')

# Configuring the app from config module
app.config.from_pyfile('config.py')

# Initializing the Flask extensions
bcrypt   = Bcrypt(app)
db       = SQLAlchemy(app)
restless = APIManager(app, flask_sqlalchemy_db=db)
manager  = Manager(app)
migrate  = Migrate(app, db)

# Importing the database models
from backend import models

# Importing the app views
from backend import views