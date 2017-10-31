# tests/support/assertions.py
import pytest
import json
import os
from jsonschema import validate


@pytest.fixture
def schema():

    """ Loads the given schema file """
    with open(os.path.join("schemas", "schema.json")) as f:
        return json.loads(f.read())


