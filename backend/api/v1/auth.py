#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    backend.api.v1.auth
    ~~~~~~~~~~~~~~~~~~~~~~~~

    This module implements the REST API v1 endpoint for authentication.
"""

from flask import request, make_response

from backend import app
from backend.api.v1 import URL
from backend.models import User


@app.route(URL + '/auth', methods=['POST'])
def authentication():
    """
    Authenticates a user.
    Request Example:
    POST
    {
        login    : 'username' or 'email address'
        password : 'password'
    }
    RESPONSE:
        200: Authenticated
        401: Unauthenticated
    """
    data      = request.get_json(force=True)
    login     = data.get('login', None)
    password  = data.get('password', None)
    criterion = [login, password, len(data) == 2]

    if not all(criterion):
        return make_response('Bad Request', 400)

    user = User.query.filter_by(username=login).first()

    if user is None:
        user = User.query.filter_by(email=login).first()

    if user and user.check_password(password):
        return make_response('Authenticated', 200)
    else:
        return make_response('Unauthenticated', 401)