#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    server.py
    ~~~~~~~~~

    This is the main module of this application.

    Flask extensions included in this application:
    - Flask-SQLAlchemy : Used for creating database models (using SQLAlchemy).
    - Flask-Bcrypt     : Used for hashing the passwords in the database.
    - Flask-Script     : Used for adding support for command-line tasks.
"""

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_script import Manager


# Creating the Flask application
app = Flask(__name__,
            template_folder='frontend/www',
            static_url_path='',
            static_folder='')

# Configuring the application from config module
app.config.from_pyfile('backend/config.py')

# Initializing the Flask extensions
db      = SQLAlchemy(app)
bcrypt  = Bcrypt(app)
manager = Manager(app)

# Importing the database models
from backend import models

# Importing the app views
from backend import views

# Importing the app manager commands
from backend import commands


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
