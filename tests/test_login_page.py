import pytest
import time

from pages.login_page import LoginPage
from tests.setup import setup

class TestLoginPage:

    def test_login_page(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        login_page = LoginPage(self.driver)
        time.sleep(10)
        login_page.set_username("Admin")
        time.sleep(10)
        login_page.set_password("admin123")
        time.sleep(10)
        login_page.click_submit()
        time.sleep(10)
        self.driver.close()
        assert True


