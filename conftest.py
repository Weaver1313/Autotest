import pytest
from Repository.basic import Api


@pytest.fixture(scope="session", autouse=True)
def api():
    api = Api(url="host")
    yield api
