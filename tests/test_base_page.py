from pages.base_page import BasePage
from tests.setup import setup
class TestBase:

    def test_base(self, setup):
        self.driver = setup
        base_page = BasePage(self.driver)
        base_page.open()
        dashboard_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        assert self.driver.current_url == dashboard_url
