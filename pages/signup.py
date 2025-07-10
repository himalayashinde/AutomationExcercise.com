from adodbapi.examples.xls_read import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.browserutils import BrowserUtils


class SignUp(BrowserUtils):

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
        self.account_banner = (By.XPATH,"//b[text()='Enter Account Information']")
        self.title_selected = (By.ID,"id_gender1")

    def validate_Label_Enter_Account_Info(self):
        label = self.wait.until(EC.visibility_of_element_located(self.account_banner))
        self.highlight(label)
        return label.is_displayed()

    def select_title(self):
        title = self.driver.find_element(*self.title_selected)
        self.highlight(title)
        title.click()
