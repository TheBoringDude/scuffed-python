from sppenv import __version__
from sppenv import load_env

import os


def test_version():
    assert __version__ == "0.1.0"


# .env is not loaded
# it should be in the top-most for testing
def test_non_env_load():
    assert os.getenv("TEST") == None
    assert os.environ.get("HELLO") == None


# .env is loaded
def test_env_load():
    load_env()

    assert os.getenv("TEST") == "123"
    assert os.environ["HELLO"] == "WORLD"
    assert os.getenv("NOT_SET_ENV") == None


# small caps variables set in .env
def test_env_smallcaps():
    load_env()

    assert os.getenv("smallvarsenv") == None
    assert os.getenv("SMALLVARSENV") == "env"


# variables with spaces
def test_env_spaces():
    load_env()

    assert os.getenv("env with spaces ") == None
    assert os.getenv("ENV_WITH_SPACES") == "value"
