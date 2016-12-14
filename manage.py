#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    manage.py
    ~~~~~~~~~
    
    This module implements the manager commands of this application.

    Commands:
    - create   : Creates all of the tables in the database.
    - drop     : Drops all of the tables from the database.
    - recreate : Drops and recreates the tables in the database.
    - db       : Performs database migrations.

    HOW TO USE:
    - Type the following in the command-line
      python3 manage.py (insert one of the commands from above here)
"""

from flask_migrate import MigrateCommand

from backend import db, manager


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


# COMMAND: recreate
@manager.command
def recreate():
    """Drops and recreates the tables in the database."""
    drop()
    create()


# COMMAND: db
manager.add_command('db', MigrateCommand)


if __name__ == "__main__":
    manager.run()