import os

import pytest


def valid_username():
    return os.getenv("VALID_USERNAME", "__missing_valid_username__")


def valid_password():
    return os.getenv("VALID_PASSWORD", "__missing_valid_password__")


def invalid_login_should_stay_on_login(page, username, password):
    page.login(username, password)
    assert page.on_login_page()
    assert page.form_is_usable()

@pytest.mark.case(id="TC01", title="Login page loads successfully", username="N/A", password="N/A", expected="Login form is displayed")
def test_tc01_login_page_loads(login_page):
    page = login_page.open()
    assert page.on_login_page()
    assert page.form_is_usable()
