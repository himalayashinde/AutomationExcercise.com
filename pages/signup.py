from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.browserutils import BrowserUtils


class SignUp(BrowserUtils):

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
        self.account_banner = (By.XPATH,"//b[text()='Enter Account Information']")

    def validate_Label_Enter_Account_Info(self):
        return self.wait.until(EC.visibility_of_element_located(self.account_banner)).is_displayed()
