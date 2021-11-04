#!/usr/bin/env python3

""" Class auth """


from flask import request
from typing import List, TypeVar


class Auth():
    """ Class Auth """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ public method require auth """
        if path is None:
            return True
        # print(path)
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        # print(excluded_paths[0])
        includes_path = excluded_paths[0]
        if path in excluded_paths or path in includes_path:
            return False
        else:
            return True
        return False

    def authorization_header(self, request=None) -> str:
        """ public method authorization header """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ public method current_user """
        return None
