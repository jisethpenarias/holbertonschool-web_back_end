#!/usr/bin/env python3

""" Class auth """


from flask import request
from typing import List, TypeVar
from os import getenv


class Auth():
    """ Class Auth """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ public method require auth """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """ public method authorization header """
        if request is None or "Authorization" not in request.headers:
            return None
        else:
            return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ public method current_user """
        return None

    def session_cookie(self, request=None):
        """ returns a cookie value from a request """
        if request:
            session = getenv('SESSION_NAME')
            return request.cookies.get(session)
        return None
