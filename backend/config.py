#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    backend.config
    ~~~~~~~~~~~~~~

    This module is used to configure this application.
"""

import os


# Flask
SECRET_KEY = os.environ.get('SECRET_KEY', 'secret_key')

# Database
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL',
    'postgresql://postgres:password@localhost:5432/app_db')
SQLALCHEMY_TRACK_MODIFICATIONS = False