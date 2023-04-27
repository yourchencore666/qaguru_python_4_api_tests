from utils.helper import BaseSession
import pytest


@pytest.fixture(scope="session")
def reqres():
    reqres_session = BaseSession(base_url="https://reqres.in/api")
    return reqres_session
