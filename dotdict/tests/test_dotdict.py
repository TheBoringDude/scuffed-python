from dotdict import __version__
from dotdict import DotDict


def test_version():
    assert __version__ == "0.1.0"


# basic usage
def test_basic_dotdict():
    dict_var = {"hello": "world"}
    a = DotDict(dict_var)
    assert a.hello == "world"


# with spacing
def test_spacing():
    dict_var = {"hello world": "message"}
    a = DotDict(dict_var)
    assert a.hello_world == "message"


# set new variable
def test_set_custom_var():
    a = DotDict()
    a.hello = "world"
    assert a.hello == "world"