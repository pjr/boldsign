import pytest
import boldsign

def test_template_list():
    boldsign.mock = True

    response = boldsign.Template.list()
