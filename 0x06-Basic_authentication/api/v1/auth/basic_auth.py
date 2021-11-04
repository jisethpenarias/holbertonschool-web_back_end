#!/usr/bin/env python3
""" Class BasicAuth """

from api.v1.auth.auth import Auth
from base64 import b64decode
from api.v1.views.users import User
from typing import TypeVar


class BasicAuth(Auth):
    """ Class BasicAuth """

    def extract_base64_authorization_header(self, authorization_header: str)\
            -> str:
        """ returns the Base64 part of the Authorization header
        for a Basic Authentication """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split(' ', 1)[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ returns the decoded value of a Base64 string
        base64_authorization_header """

        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            return b64decode(base64_authorization_header).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ eturns the user email and password from the Base64
        decoded value """

        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None
        decoded_value = decoded_base64_authorization_header.split(":", 1)
        # print(decoded_value[1])
        email = decoded_value[0]
        password = decoded_value[1]
        return email, password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ eturns the User instance based on his email and password. """

        if user_email is None or user_pwd is None:
            return None
        if not isinstance(user_email, str) or not isinstance(user_pwd, str):
            return None
        try:
            search_users = User.search({'email': user_email})
        except Exception:
            return None

        for user in search_users:
            if user.is_valid_password(user_pwd):
                return user

        return None
