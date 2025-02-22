import unittest
from api_tester.client import MakeAPICall
from api_tester.auth import TokenAuth

class TestAPIClient(unittest.TestCase):
    def setUp(self):
        token_auth = TokenAuth("test_token")
        self.client = MakeAPICall("https://jsonplaceholder.typicode.com", auth_strategy=token_auth)

    def test_get(self):
        response = self.client.request("GET", "/posts/1")
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        response = self.client.request("POST", "/posts", json={"title": "test", "body": "content", "userId": 1})
        self.assertEqual(response.status_code, 201)

if __name__ == "__main__":
    unittest.main()
