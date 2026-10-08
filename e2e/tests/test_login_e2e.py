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

@pytest.mark.case(id="TC02", title="Username field is visible", username="N/A", password="N/A", expected="Username input is visible")
def test_tc02_username_field_is_visible(login_page):
    page = login_page.open()
    assert page.username_element().is_displayed()

@pytest.mark.case(id="TC03", title="Password field is visible", username="N/A", password="N/A", expected="Password input is visible")
def test_tc03_password_field_is_visible(login_page):
    page = login_page.open()
    assert page.password_element().is_displayed()

@pytest.mark.case(id="TC04", title="Password input type is password", username="N/A", password="N/A", expected="Password input masks typed text")
def test_tc04_password_input_type_is_password(login_page):
    page = login_page.open()
    assert page.password_element().get_attribute("type") == "password"

@pytest.mark.case(id="TC05", title="Login button is visible", username="N/A", password="N/A", expected="Login button is visible")
def test_tc05_login_button_is_visible(login_page):
    page = login_page.open()
    assert page.login_button().is_displayed()

@pytest.mark.case(id="TC06", title="Login button is enabled", username="N/A", password="N/A", expected="Login button is enabled")
def test_tc06_login_button_is_enabled(login_page):
    page = login_page.open()
    assert page.login_button().is_enabled()

@pytest.mark.case(id="TC07", title="Username field accepts text", username="student01", password="N/A", expected="Username value matches typed text")
def test_tc07_username_field_accepts_text(login_page):
    page = login_page.open()
    page.enter_username("student01")
    assert page.username_value() == "student01"

@pytest.mark.case(id="TC08", title="Password field accepts text", username="N/A", password="SamplePassword", expected="Password value matches typed text")
def test_tc08_password_field_accepts_text(login_page):
    page = login_page.open()
    page.enter_password("SamplePassword")
    assert page.password_value() == "SamplePassword"

@pytest.mark.case(id="TC09", title="Username can be cleared", username="student01", password="N/A", expected="Username field becomes empty after clear")
def test_tc09_username_can_be_cleared(login_page):
    page = login_page.open()
    page.enter_username("student01").clear(page.USERNAME)
    assert page.username_value() == ""

@pytest.mark.case(id="TC10", title="Password can be cleared", username="N/A", password="SamplePassword", expected="Password field becomes empty after clear")
def test_tc10_password_can_be_cleared(login_page):
    page = login_page.open()
    page.enter_password("SamplePassword").clear(page.PASSWORD)
    assert page.password_value() == ""
