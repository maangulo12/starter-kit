#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    backend.config
    ~~~~~~~~~~~~~~

    This module contains the configuration values of this application.

    For more information on how to handle configuration:
    - Flask            : http://flask.pocoo.org/docs/0.11/config/
    - Flask-SQLAlchemy : http://flask-sqlalchemy.pocoo.org/2.1/config/
"""

import os


# Flask configuration values
SECRET_KEY = os.environ.get('SECRET_KEY', 'secret_key')
DEBUG      = os.environ.get('DEBUG', True)

# Flask-SQLAlchemy configuration values
SQLALCHEMY_DATABASE_URI        = os.environ.get('DATABASE_URL', 'postgresql://postgres:password@localhost:5432/app_db')
SQLALCHEMY_TRACK_MODIFICATIONS = False