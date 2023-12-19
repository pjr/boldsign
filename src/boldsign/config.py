
class BoldsignConfig:
    api_url = "https://api.boldsign.com/v1/"

    @property
    def api_key(self):
        from boldsign import api_key
        return api_key

    @property
    def trace(self):
        from boldsign import trace
        return trace

    @property
    def mock(self):
        from boldsign import mock
        return mock

config = BoldsignConfig()
