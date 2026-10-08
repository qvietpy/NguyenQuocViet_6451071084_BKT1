from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from e2e.pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://vanphongdientu.utc.edu.vn/Login"

    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "userpwd")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input.submit_login")
    REMEMBER_CHECKBOX = (By.ID, "persistent")
    REMEMBER_LABEL = (By.CSS_SELECTOR, "label.check")
    EMAIL_UTC_LOGIN = (By.XPATH, "//a[contains(normalize-space(), 'e-mail UTC')]")
    FORGOT_PASSWORD = (By.CSS_SELECTOR, "a[href='/Login/GetPass']")
    LOGIN_FORM = (By.CSS_SELECTOR, "form[action='/Login']")
    ERROR_MESSAGE = (
        By.XPATH,
        "//*[contains(normalize-space(), 'Tài khoản') and "
        "contains(normalize-space(), 'mật khẩu') and "
        "contains(normalize-space(), 'không đúng')]",
    )

    def open(self):
        self.driver.get(self.URL)
        self.wait_present(self.LOGIN_FORM)
        return self

    def username_element(self):
        return self.wait_visible(self.USERNAME)

    def password_element(self):
        return self.wait_visible(self.PASSWORD)

    def login_button(self):
        return self.wait_clickable(self.LOGIN_BUTTON)

    def enter_username(self, username):
        return self.type(self.USERNAME, username)

    def enter_password(self, password):
        return self.type(self.PASSWORD, password)

    def set_credentials(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        return self

    def click_login(self):
        return self.click(self.LOGIN_BUTTON)

    def login(self, username, password):
        self.set_credentials(username, password)
        self.click_login()
        return self

    def submit_with_enter(self):
        return self.press_enter(self.PASSWORD)

    def remember_selected(self):
        return self.wait_present(self.REMEMBER_CHECKBOX).is_selected()

    def toggle_remember(self):
        self.click(self.REMEMBER_LABEL)
        return self

    def email_utc_login_visible(self):
        return self.is_displayed(self.EMAIL_UTC_LOGIN)

    def click_email_utc_login(self):
        return self.click(self.EMAIL_UTC_LOGIN)

    def forgot_password_visible(self):
        return self.is_displayed(self.FORGOT_PASSWORD)

    def click_forgot_password(self):
        return self.click(self.FORGOT_PASSWORD)

    def error_visible(self, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.ERROR_MESSAGE)
            )
            return True
        except TimeoutException:
            return False

    def error_text(self):
        return self.get_text(self.ERROR_MESSAGE)

    def on_login_page(self):
        return "/login" in self.current_url().lower()

    def login_successful(self, timeout=8):
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: "/login" not in driver.current_url.lower()
            )
            return True
        except TimeoutException:
            return False

    def form_is_usable(self):
        def usable():
            try:
                return (
                    self.is_displayed(self.LOGIN_FORM)
                    and self.username_element().is_enabled()
                    and self.password_element().is_enabled()
                    and self.login_button().is_enabled()
                )
            except StaleElementReferenceException:
                return False

        try:
            return WebDriverWait(self.driver, self.timeout).until(lambda _driver: usable())
        except TimeoutException:
            return False

    def wait_after_submit(self):
        WebDriverWait(self.driver, self.timeout).until(
            lambda _driver: self.error_visible(timeout=1)
            or not self.on_login_page()
            or self.form_is_usable()
        )

    def username_value(self):
        return self.get_attribute(self.USERNAME, "value")

    def password_value(self):
        return self.get_attribute(self.PASSWORD, "value")
