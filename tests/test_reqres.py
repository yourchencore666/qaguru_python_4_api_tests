import requests
from requests import Response
from pytest_voluptuous import S

from schemas.reqresin import list_user_schema


def test_get_users_page_number():
    url = "https://reqres.in/api/users"

    response: Response = requests.get(url, params={"page": 2})

    assert response.status_code == 200
    assert response.json()["page"] == 2


def test_get_user_on_page():
    url = "https://reqres.in/api/users"

    response: Response = requests.get(url, params={"page": 2})

    per_page = response.json()["per_page"]
    data_len = len(response.json()["data"])
    assert data_len == per_page


def test_get_users_validate_schema():
    url = "https://reqres.in/api/users"

    response: Response = requests.get(url, params={"page": 2})

    assert S(list_user_schema) == response.json()
