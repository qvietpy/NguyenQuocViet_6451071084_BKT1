import os

from selenium import webdriver


class BaseTest:
    PAGE_LOAD_TIMEOUT = 30
    DEFAULT_TIMEOUT = 10

    @staticmethod
    def create_chrome_options():
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")

        if os.getenv("HEADLESS", "0") == "1":
            options.add_argument("--headless=new")
            options.add_argument("--window-size=1920,1080")

        return options

    @classmethod
    def create_driver(cls):
        driver = webdriver.Chrome(options=cls.create_chrome_options())
        driver.set_page_load_timeout(cls.PAGE_LOAD_TIMEOUT)
        return driver
