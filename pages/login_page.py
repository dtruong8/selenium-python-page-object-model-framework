from selenium.webdriver.common.by import By

class LoginPage:
    username_xpath = "(//input[@placeholder='Username'])[1]"
    password_xpath = "(//input[@placeholder='Password'])[1]"
    submit_btn_xpath = "(//button[normalize-space()='Login'])[1]"

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(By.XPATH, self.username_xpath).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)

    def click_submit(self):
        self.driver.find_element(By.XPATH, self.submit_btn_xpath).click()
