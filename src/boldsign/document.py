from .resource import BoldsignResource

class Document(BoldsignResource):
    @classmethod
    def list(cls, **params):
        return cls.request(
            "GET",
            "document/list",
            params=params
        )
