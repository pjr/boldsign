import os
import requests

class Client:
    API_HOSTNAME = "api.boldsign.com"
    API_BASE = f"https://{API_HOSTNAME}/v1/"

    def __init__(self, api_key=None):
        self.api_key = api_key
        if not self.api_key:
            raise ValueError("An API key is required to access Boldsign.")

        self.session = requests.Session()
        self.session.headers.update({
            "X-API-KEY": self.api_key
        })

    def _request(self, method, endpoint, **kwargs):
        url = f"{self.API_BASE}{endpoint}"
        response = self.session.request(method, url, **kwargs)
        response.raise_for_status()
        return response.json()

    def list(self):
        return self._request(
            "GET",
            "document/list"
        )
