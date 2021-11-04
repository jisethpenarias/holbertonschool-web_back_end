#!/usr/bin/env python3

""" Class auth """


from flask import request
from typing import List, TypeVar


class Auth():
    """ Class Auth """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ public method require auth """
        if path and excluded_paths:
            if path[-1] != '/':
                path += '/'
            for pth in excluded_paths:

                path = path.replace('/', '')
                pth = pth.replace('/', '')

                if pth[-1] == '*':
                    pth = pth.replace('*', '.*')

                if re.search(pth, path):
                    return False
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
