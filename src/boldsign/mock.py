import os
import json
import responses

class MockResponse:
    def __init__(self, resp_dir="mock_responses"):
        self.resp_dir = resp_dir

    def load(self, url):
        url_split = url.lower().split('/')

        base_dir = os.path.dirname(os.path.abspath(__file__))
        filename = f"{self.resp_dir}/{url_split[-2]}/{url_split[-1]}.json"
        filepath = os.path.join(base_dir, filename)
        with open(filepath, "r") as fh:
            return json.loads(fh.read())

class MockContextManager:
    def __init__(self, mock_enabled, method, url):
        self.mock_enabled = mock_enabled
        self.mock_response = MockResponse()
        self.url = url
        self.method = method

    def __enter__(self):
        if self.mock_enabled:
            self.resp = responses.RequestsMock()
            self.resp.start()
            body = self.mock_response.load(self.url)
            self.resp.add(
                method=self.method,
                url=self.url,
                json=body,
                status=200
            )

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.mock_enabled and self.resp:
            self.resp.stop()
            self.resp.reset()
