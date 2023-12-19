import os
from .resource import BoldsignResource

class Template(BoldsignResource):
    @classmethod
    def list(cls, **params):
        return cls.request(
            "GET",
            "template/list",
            params=params
        )

    @classmethod
    def create_embed(cls, **kwargs):
        # deal with roles
        roles = kwargs.pop('Roles', [])

        data = {k: str(v).lower() if isinstance(v, bool) else v for k, v in kwargs.items()}

        for i, role in enumerate(roles):
            for key, value in role.items():
                data[f'Roles[{i}][{key}]'] = value

        # handle files
        filepath = kwargs.pop("Files", None)
        filename = os.path.basename(filepath)

        files=[
            ('Files',(filename,open(filepath,'rb'),'application/pdf'))
        ]

        return cls.request(
            "POST",
            "template/createEmbeddedTemplateUrl",
            data=data,
            files=files
        )
