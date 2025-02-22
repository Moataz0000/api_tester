import  requests
from api_tester.auth import AuthStrategy
from api_tester.factory import APIRequestFactory


class MakeAPICall:
    def __init__(self, base_url, auth_strategy=None):
        self.base_url = base_url
        self.session = requests.Session()

        if auth_strategy and isinstance(auth_strategy, AuthStrategy):
            auth_strategy.apply(self.session)

    def request(self, method, endpoint, **kwargs):
        api_request = APIRequestFactory.create_request(method, self.base_url, endpoint, **kwargs)
        return api_request.send()
