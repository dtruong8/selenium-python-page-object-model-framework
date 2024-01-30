
class BasePage:
    def __init__(self, driver, base_url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"):
        self.driver = driver
        self.base_url = base_url

    def open(self):
        self.driver.get(self.base_url)

