#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    backend.views
    ~~~~~~~~~~~~~

    This module implements the views of this application.
"""

from flask import render_template

from backend import app


@app.route('/')
def index():
    """This is the first view of this application."""
    return render_template('index.html')