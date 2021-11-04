#!/usr/bin/env python3

""" Class auth """


from flask import request
from typing import List, TypeVar


class Auth():
    """ Class Auth """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ public method require auth """
        return False

    def authorization_header(self, request=None) -> str:
        """ public method authorization header """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ public method current_user """
        return None
