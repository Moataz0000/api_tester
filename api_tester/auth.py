from requests.auth import HTTPBasicAuth


class AuthStrategy:
    """Base Authentication Strategy"""

    def apply(self, session):
        pass


class BasicAuth(AuthStrategy):
    def __init__(self, username, password):
        self.auth = HTTPBasicAuth(username, password)

    def apply(self, session):
        session.auth = self.auth



class TokenAuth(AuthStrategy):
    def __init__(self, token):
        self.token = token

    def apply(self, session):
        session.headers.update({"Authorization": f"Token {self.token}"})


class OAuth(AuthStrategy):
    def __init__(self, token):
        self.token = token

    def apply(self, session):
        session.headers.update({"Authorization": f"Bearer {self.token}"})