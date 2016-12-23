#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    backend.views
    ~~~~~~~~~~~~~

    This module implements the views of this application.
"""

from flask import render_template

from backend import app


@app.route('/', defaults={'path': ''})
@app.route('/<path>')
def index(path):
    """
    This is the only view that the backend needs to serve.
    Single-page applications only serve one page.
    """
    return render_template('index.html')