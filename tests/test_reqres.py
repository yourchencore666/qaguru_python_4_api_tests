import requests
from requests import Response
from pytest_voluptuous import S

from schemas.reqresin import list_user_schema, user_schema, resource_schema


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


def test_get_list_users_validate_schema():
    url = "https://reqres.in/api/users"

    response: Response = requests.get(url, params={"page": 2})

    assert S(list_user_schema) == response.json()


def test_get_users_validate_schema():
    url = "https://reqres.in/api/users"

    response: Response = requests.get(url, params={"page": 2})

    assert S(user_schema) in response.json()["data"]


def test_get_users_text_validate():
    url = "https://reqres.in/api/users"

    response: Response = requests.get(url, params={"page": 2})

    assert response.json()["support"]["text"] == "To keep ReqRes free, " \
                                                 "contributions towards server costs are appreciated!"


def test_get_single_user_healthcheck():
    url = "https://reqres.in/api/users/2"

    response: Response = requests.get(url)

    assert response.status_code == 200
    assert response.json() is not None


def test_get_single_user_validate_schema():
    url = "https://reqres.in/api/users/2"

    response: Response = requests.get(url)

    assert S(user_schema) == response.json()["data"]


def test_get_single_user_not_found():
    url = "https://reqres.in/api/users/23"

    response: Response = requests.get(url)

    assert response.status_code == 404


def test_get_single_user_not_found_negative():
    url = "https://reqres.in/api/users/23"

    response: Response = requests.get(url)

    assert response.status_code != 200
    assert response.json() == {}


def test_get_list_resources_validate_schema():
    url = "https://reqres.in/api/unknown"

    response: Response = requests.get(url)

    assert S(resource_schema) in response.json()["data"]
