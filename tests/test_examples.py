# tests/support/assertions.py
import pytest
import json
import os
from jsonschema import validate
from os import listdir

EXAMPLES = os.path.join(os.path.dirname(__file__), "examples")


def load_json(filename):
    """ Loads the given schema file """
    with open(filename) as schema_file:
        return json.loads(schema_file.read())


@pytest.mark.parametrize("data_source", [os.path.join(EXAMPLES, f) for f in listdir(EXAMPLES)])
def test_examples(schema, data_source):
    data = load_json(data_source)
    validate(data, schema)
