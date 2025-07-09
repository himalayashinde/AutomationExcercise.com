from selenium.webdriver.common.by import By

from utils.browserutils import BrowserUtils


class HomePage(BrowserUtils):

    def __init__(self,driver):
        self.driver = driver
        self.signup_login_link= (By.XPATH, "//a[text()=' Signup / Login']")


    def click_signup_login(self):
        self.driver.find_element(*self.signup_login_link).click()

