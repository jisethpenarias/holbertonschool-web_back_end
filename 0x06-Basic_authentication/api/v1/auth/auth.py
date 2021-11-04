#!/usr/bin/env python3

""" Class auth """


from flask import request
from typing import List, TypeVar


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
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ public method current_user """
        return None
