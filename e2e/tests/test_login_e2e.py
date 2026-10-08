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

@pytest.mark.case(id="TC11", title="Submit empty username and password", username="", password="", expected="Form remains usable on login page")
def test_tc11_submit_empty_username_and_password(login_page):
    page = login_page.open()
    page.click_login()
    assert page.on_login_page()
    assert page.form_is_usable()

@pytest.mark.case(id="TC12", title="Submit empty username", username="", password="wrong-password", expected="Form remains on login page")
def test_tc12_submit_empty_username(login_page):
    page = login_page.open()
    invalid_login_should_stay_on_login(page, "", "wrong-password")

@pytest.mark.case(id="TC13", title="Submit empty password", username="wrong-user", password="", expected="Form remains on login page")
def test_tc13_submit_empty_password(login_page):
    page = login_page.open()
    invalid_login_should_stay_on_login(page, "wrong-user", "")

@pytest.mark.case(id="TC14", title="Username contains spaces only", username="   ", password="wrong-password", expected="Spaces-only username is not accepted")
def test_tc14_username_contains_spaces_only(login_page):
    page = login_page.open()
    invalid_login_should_stay_on_login(page, "   ", "wrong-password")

@pytest.mark.case(id="TC15", title="Password contains spaces only", username="wrong-user", password="   ", expected="Spaces-only password is not accepted")
def test_tc15_password_contains_spaces_only(login_page):
    page = login_page.open()
    invalid_login_should_stay_on_login(page, "wrong-user", "   ")

@pytest.mark.case(id="TC16", title="Both username and password spaces only", username="   ", password="   ", expected="Spaces-only credentials are not accepted")
def test_tc16_both_username_password_spaces_only(login_page):
    page = login_page.open()
    invalid_login_should_stay_on_login(page, "   ", "   ")

@pytest.mark.case(id="TC17", title="Invalid username and invalid password", username="invalid-user", password="invalid-password", expected="Invalid credentials are rejected")
def test_tc17_invalid_username_and_invalid_password(login_page):
    page = login_page.open()
    invalid_login_should_stay_on_login(page, "invalid-user", "invalid-password")

@pytest.mark.case(id="TC18", title="Format-like username and wrong password", username="2021000000", password="wrong-password", expected="Format-like invalid credentials are rejected")
def test_tc18_format_like_username_wrong_password(login_page):
    page = login_page.open()
    invalid_login_should_stay_on_login(page, "2021000000", "wrong-password")

@pytest.mark.case(id="TC19", title="One-character username", username="a", password="wrong-password", expected="One-character username is rejected")
def test_tc19_one_character_username(login_page):
    page = login_page.open()
    invalid_login_should_stay_on_login(page, "a", "wrong-password")

@pytest.mark.case(id="TC20", title="One-character password", username="wrong-user", password="a", expected="One-character password is rejected")
def test_tc20_one_character_password(login_page):
    page = login_page.open()
    invalid_login_should_stay_on_login(page, "wrong-user", "a")

@pytest.mark.case(id="TC21", title="Very long username", username="long username", password="wrong-password", expected="Very long username is handled without breaking the form")
def test_tc21_very_long_username(login_page):
    page = login_page.open()
    invalid_login_should_stay_on_login(page, "u" * 256, "wrong-password")

@pytest.mark.case(id="TC22", title="Very long password", username="wrong-user", password="long password", expected="Very long password is handled without breaking the form")
def test_tc22_very_long_password(login_page):
    page = login_page.open()
    invalid_login_should_stay_on_login(page, "wrong-user", "p" * 256)

@pytest.mark.case(id="TC23", title="Leading whitespace username", username=" invalid-user", password="wrong-password", expected="Leading-whitespace username is rejected")
def test_tc23_leading_whitespace_username(login_page):
    page = login_page.open()
    invalid_login_should_stay_on_login(page, " invalid-user", "wrong-password")
