#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    server.py
    ~~~~~~~~~

    This module is used to run the application.
"""

from backend import app


if __name__ == "__main__":
    # Run the application
    app.run(host='0.0.0.0', port=5000)