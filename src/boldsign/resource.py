import requests
import responses

from boldsign.config import config
from boldsign.exception import BoldsignError
from boldsign.mock import MockContextManager
from boldsign.response import BoldsignObject

class BoldsignResource:
    @classmethod
    def request(cls, method, url, params=None, headers=None, data=None,
                files=None):
        if headers is None:
            headers = {}

        if config.api_key:
            headers["X-API-KEY"] = config.api_key

        uri = f"{config.api_url}{url}"

        with MockContextManager(config.mock, method, uri):
            response = requests.request(
                method,
                uri,
                params=params,
                data=data,
                headers=headers,
                files=files,
                hooks={'response': BoldsignResource.request_verbose}
            )
            cls.raise_for_status(response)
            return BoldsignObject(response)

    @classmethod
    def raise_for_status(cls, response):
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_err:
            raise BoldsignError(response)

    @staticmethod
    def request_verbose(response, *args, **kwargs):
        if config.trace:
            print(f"Request headers: {response.request.headers}")
            print(f"Request body: {response.request.body}")
            print(f"Response headers: {response.headers}")
            print(f"Response body: {response.text}")
