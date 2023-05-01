from utils.helper import BaseSession
import pytest
from dotenv import load_dotenv
from selene.support.shared import browser
import os
import requests

load_dotenv()

LOGIN = os.getenv('user_login')
PASSWORD = os.getenv('user_password')
API_URL = os.getenv('api_url')
WEB_URL = os.getenv('web_url')

browser.config.base_url = WEB_URL


@pytest.fixture(scope="session")
def reqres():
    reqres_session = BaseSession(base_url="https://reqres.in/api")
    return reqres_session


@pytest.fixture(scope="session")
def demowebshop():
    browser.open("")
    response = requests.post(
        url=API_URL + '/login',
        params={'Email': LOGIN, 'Password': PASSWORD},
        headers={'content-type': "application/x-www-form-urlencoded; charset=UTF-8"},
        allow_redirects=False
    )

    authorization_cookie = response.cookies.get('NOPCOMMERCE.AUTH')
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": authorization_cookie})
    return browser.driver.get_cookies()
