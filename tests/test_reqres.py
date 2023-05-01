from pytest_voluptuous import S
from requests import Response
from schemas.reqresin import list_user_schema, user_schema, resource_schema, created_user_schema, updated_user_schema, \
    register_schema
from datetime import datetime


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


def test_create_user(reqres):
    response: Response = reqres.post(
        url='/users',
        data={
            "name": "morpheus",
            "job": "leader"
        },
        allow_redirects=False
    )
    assert response.status_code >= 200 <= 299


def test_create_user_schema_validate(reqres):
    response: Response = reqres.post(
        url='/users',
        data={
            "name": "morpheus",
            "job": "leader"
        },
        allow_redirects=False
    )
    assert S(created_user_schema) == response.json()


def test_update_user(reqres):
    response: Response = reqres.put(
        url='/users/2',
        data={
            "name": "morpheus",
            "job": "zion resident"
        },
        allow_redirects=False
    )
    response_date = datetime.strptime(response.headers['Date'], '%a, %d %b %Y %H:%M:%S %Z')
    formatted_date = response_date.strftime('%Y-%m-%dT%H:%M:%S.{:03d}Z').format(response_date.microsecond // 1000)

    assert response.status_code >= 200 <= 299
    assert response.json()['name'] == 'morpheus'
    assert response.json()['job'] == 'zion resident'
    assert response.json()['updatedAt'] == formatted_date


def test_update_user_schema_validate(reqres):
    response: Response = reqres.put(
        url='/users/2',
        data={
            "name": "morpheus",
            "job": "zion resident"
        },
        allow_redirects=False
    )

    assert S(updated_user_schema) == response.json()


def test_register_successful(reqres):
    response: Response = reqres.post(
        url='/register',
        data={
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        },
        allow_redirects=False
    )
    assert response.status_code >= 200 <= 299
    assert response.json()['id'] is not None
    assert response.json()['token'] is not None


def test_register_successful_schema(reqres):
    response: Response = reqres.post(
        url='/register',
        data={
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        },
        allow_redirects=False
    )

    assert S(register_schema) == response.json()


def test_register_unsuccessful_missing_password(reqres):
    response: Response = reqres.post(
        url='/register',
        data={
            "email": "eve.holt@reqres.in"
        },
        allow_redirects=False
    )
    assert response.status_code == 400
    assert response.json()['error'] == "Missing password"


def test_register_unsuccessful_missing_email(reqres):
    response: Response = reqres.post(
        url='/register',
        data={
            "password": "pistol"
        },
        allow_redirects=False
    )
    assert response.status_code == 400
    assert response.json()['error'] == "Missing email or username"


def test_login_successful(reqres):
    response: Response = reqres.post(
        url='/login',
        data={
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        },
        allow_redirects=False
    )
    assert response.status_code >= 200 <= 299
    assert response.json()['token'] is not None


def test_login_unsuccessful_missing_password(reqres):
    response: Response = reqres.post(
        url='/login',
        data={
            "email": "eve.holt@reqres.in"
        },
        allow_redirects=False
    )
    assert response.status_code == 400
    assert response.json()['error'] == "Missing password"


def test_login_unsuccessful_missing_email(reqres):
    response: Response = reqres.post(
        url='/login',
        data={
            "password": "pistol"
        },
        allow_redirects=False
    )
    assert response.status_code == 400
    assert response.json()['error'] == "Missing email or username"
