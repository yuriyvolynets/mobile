import pytest
from sys import path as sys_path
from os.path import abspath

def pytest_addoption(parser):
    parser.addoption("--taf", action="store", default=None, help="Set path to the TAF folder")

def pytest_runtest_setup(item):
    taf_path = item.config.getoption("--taf")
    if taf_path is None:
        pytest.fail("TAF path is not specified.")
    sys_path.insert(0, abspath(taf_path))

@pytest.fixture
def mobile_app(request):
    try:
        return getattr(__import__("base.general", fromlist=["base.general"]), "General")()
    except ImportError:
        raise Exception("Can't import module, please check path to the testing framework")
