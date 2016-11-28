#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    server.py
    ~~~~~~~~~

    This is the main module of this application.

    Flask extensions included in this application:
    - Flask-SQLAlchemy : Used for creating database models (using SQLAlchemy).
    - Flask-Bcrypt     : Used for hashing the passwords in the database.
"""

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


# Creating the Flask application
app = Flask(__name__,
            template_folder='frontend/www',
            static_url_path='',
            static_folder='')

# Configuring the application from config module
app.config.from_pyfile('backend/config.py')

# Initializing the Flask extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Importing database models
from backend import models

# Initial view of this application
@app.route('/')
def index():
    """Render the initial view."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
