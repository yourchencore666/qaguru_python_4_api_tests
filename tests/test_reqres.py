from pytest_voluptuous import S
from requests import Response
from schemas.reqresin import list_user_schema, user_schema, resource_schema


def test_get_users_page_number(reqres):
    response: Response = reqres.get("/users?page=2")

    assert response.status_code == 200
    assert response.json()["page"] == 2


def test_get_user_on_page(reqres):
    response: Response = reqres.get("/users")

    per_page = response.json()["per_page"]
    data_len = len(response.json()["data"])
    assert data_len == per_page


def test_get_list_users_validate_schema(reqres):
    response: Response = reqres.get("/users")

    assert S(list_user_schema) == response.json()


def test_get_users_validate_schema(reqres):
    response: Response = reqres.get("/users")

    assert S(user_schema) in response.json()["data"]


def test_get_users_text_validate(reqres):
    response: Response = reqres.get("/users")

    assert response.json()["support"]["text"] == "To keep ReqRes free, " \
                                                 "contributions towards server costs are appreciated!"


def test_get_single_user_healthcheck(reqres):
    response: Response = reqres.get("/users/2")

    assert response.status_code == 200
    assert response.json() is not None


def test_get_single_user_validate_schema(reqres):
    response: Response = reqres.get("/users/2")

    assert S(user_schema) == response.json()["data"]


def test_get_single_user_not_found(reqres):
    response: Response = reqres.get("/users/23")
    assert response.status_code == 404


def test_get_single_user_not_found_negative(reqres):
    response: Response = reqres.get("/users/23")

    assert response.status_code != 200
    assert response.json() == {}


def test_get_list_resources_validate_schema(reqres):
    response: Response = reqres.get("/unknown")

    assert S(resource_schema) in response.json()["data"]
