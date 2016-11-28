#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    backend.commands
    ~~~~~~~~~~~~~~~~

    This module implements the manager commands of this application.

    For more information on how to create commands:
    - Flask-Script : https://flask-script.readthedocs.io/en/latest/

    Commands:
    - create : Creates all of the tables in the database.
    - drop   : Drops all of the tables from the database.
"""

from backend import manager, db


# COMMAND: create
@manager.command
def create():
    """Creates all of the tables in the database."""
    db.create_all()
    print('Created all of the tables in the database.')


# COMMAND: drop
@manager.command
def drop():
    """Drops all of the tables from the database."""
    db.drop_all()
    print('Dropped all of the tables from the database.')


# More commands can be added here...
