#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    backend.api.v1.endpoints
    ~~~~~~~~~~~~~~~~~~~~~~~~

    This module implements the REST API v1 endpoints of this application.
"""

from backend import restless

from backend.api.v1 import URL
from backend.models import User


# ENDPOINT: /api/v1/users
restless.create_api(User, methods          = ['GET', 'POST', 'DELETE', 'PUT'],
                          url_prefix       = URL,
                          collection_name  = 'users',
                          results_per_page = 0)