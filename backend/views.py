#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    backend.views
    ~~~~~~~~~~~~~

    This module implements the views of this application.
"""

from ..server import app


@app.route('/')
def index():
    """This is the initial view of this application."""
    return render_template('index.html')
