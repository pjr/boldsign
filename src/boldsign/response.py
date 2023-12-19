import json

class BoldsignObject:
    _dict = []
    _response = None

    def __init__(self, response):
        self._response = response
        data = response.json()
        for key, value in data.items():
            setattr(self, key, value)
            self._dict.append(key)

    def properties(self):
        return self._dict

    def dump(self):
        return self._response
