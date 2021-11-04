#!/usr/bin/env python3
""" Class BasicAuth """

from api.v1.auth.auth import Auth
from base64 import b64decode


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
