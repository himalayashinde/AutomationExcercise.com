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
        self.reg_name=(By.ID,"name")
        self.reg_email = (By.ID, "email")
        self.reg_password = (By.ID, "password")


    def validate_Label_Enter_Account_Info(self):
        label = self.wait.until(EC.visibility_of_element_located(self.account_banner))
        self.highlight(label)
        return label.is_displayed()

    def select_title(self):
        title = self.driver.find_element(*self.title_selected)
        self.highlight(title)
        title.click()


    def set_name(self,username):
        name_field= self.driver.find_element(*self.reg_name)
        self.highlight(name_field)
        name_field.clear()
        name_field.send_keys(username)


    def set_email(self,user_email):
        email_field = self.driver.find_element(*self.reg_email)
        self.highlight(email_field)
        email_field.clear()
        email_field.send_keys(user_email)


    def set_password(self,user_password):
        password_field= self.driver.find_element(*self.reg_password)
        self.highlight(password_field)
        password_field.send_keys(user_password)

