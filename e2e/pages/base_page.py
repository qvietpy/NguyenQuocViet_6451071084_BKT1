from selenium.common.exceptions import (
    StaleElementReferenceException,
    TimeoutException,
    WebDriverException,
)
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)

    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_present(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find(self, locator):
        return self.wait_present(locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.wait_clickable(locator).click()
        return self

    def type(self, locator, text):
        def action():
            try:
                element = self.wait_visible(locator)
                element.clear()
                element.send_keys(text)
                return True
            except (StaleElementReferenceException, WebDriverException):
                return False

        WebDriverWait(self.driver, self.timeout).until(lambda _driver: action())
        return self

    def clear(self, locator):
        def action():
            try:
                self.wait_visible(locator).clear()
                return True
            except (StaleElementReferenceException, WebDriverException):
                return False

        WebDriverWait(self.driver, self.timeout).until(lambda _driver: action())
        return self

    def get_text(self, locator):
        return self.wait_visible(locator).text

    def get_attribute(self, locator, attribute):
        return self.wait_present(locator).get_attribute(attribute)

    def is_displayed(self, locator):
        try:
            return self.wait_visible(locator).is_displayed()
        except (StaleElementReferenceException, TimeoutException):
            return False

    def is_enabled(self, locator):
        try:
            return self.wait_present(locator).is_enabled()
        except (StaleElementReferenceException, TimeoutException):
            return False

    def current_url(self):
        return self.driver.current_url

    def refresh(self):
        self.driver.refresh()
        return self

    def press_enter(self, locator):
        self.wait_visible(locator).send_keys(Keys.ENTER)
        return self

    def element_exists(self, locator):
        try:
            self.wait_present(locator)
            return True
        except TimeoutException:
            return False

    def url_contains(self, value):
        try:
            WebDriverWait(self.driver, self.timeout).until(EC.url_contains(value))
            return True
        except TimeoutException:
            return False

    def wait_url_change(self, old_url):
        return WebDriverWait(self.driver, self.timeout).until(EC.url_changes(old_url))
