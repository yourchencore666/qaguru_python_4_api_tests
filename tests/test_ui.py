import os

from allure_commons._allure import step
from dotenv import load_dotenv
from selene import have
from selene.support.shared import browser

load_dotenv()

LOGIN = os.getenv('user_login')
PASSWORD = os.getenv('user_password')


def test_login(reqres):
    """Successful authorization to some demowebshop (UI)"""
    with step("Open login page"):
        browser.open("/login")

    with step("Fill login form"):
        browser.element("#Email").send_keys(LOGIN)
        browser.element("#Password").send_keys(PASSWORD).press_enter()

    with step("Verify successful authorization"):
        browser.element(".account").should(have.text(LOGIN))


def test_login_through_api(demowebshop):
    """Successful authorization to some demowebshop (UI)"""

    browser.open("/Themes/DefaultClean/Content/images/logo.png")

    browser.open("")

    with step("Verify successful authorization"):
        browser.element(".account").should(have.text(LOGIN))
