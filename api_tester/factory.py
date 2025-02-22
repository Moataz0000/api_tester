import requests




class APIRequest:
    """Base class for API requests."""

    def __init__(self, base_url, endpoint, **kwargs):
        self.url = f'{base_url}{endpoint}'
        self.kwargs = kwargs

    def send(self):
        raise NotImplementedError("Subclasses must implement the send method")



class GetRequest(APIRequest):
    def send(self):
        return requests.get(self.url, **self.kwargs)


class PostRequest(APIRequest):
    def send(self):
        return requests.post(self.url, **self.kwargs)


class PutRequest(APIRequest):
    def send(self):
        return requests.put(self.url, **self.kwargs)

class PatchRequest(APIRequest):
    def send(self):
        return requests.patch(self.url, **self.kwargs)

class DeleteRequest(APIRequest):
    def send(self):
        return requests.delete(self.url, **self.kwargs)



class APIRequestFactory:
    """Factory class to generate API Requests dynamically."""
    request_types = {
        "GET": GetRequest,
        "POST": PostRequest,
        "PUT": PutRequest,
        "PATCH": PatchRequest,
        "DELETE": DeleteRequest,
    }


    def create_request(method, base_url, endpoint, **kwargs):
        request_class = APIRequestFactory.request_types.get(method.upper())
        if not request_class:
            raise ValueError(f"Unsupported HTTP method: {method}")
        return request_class(base_url, endpoint, **kwargs)