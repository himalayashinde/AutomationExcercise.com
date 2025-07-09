from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.browserutils import BrowserUtils


# 5. Verify 'New User Signup!' is visible
    # 6. Enter name and email address
    # 7. Click 'Signup' button

class LoginPage(BrowserUtils):

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.signupName =(By.CSS_SELECTOR, "div[class='signup-form'] input[name='name']")
        self.signupEmail = (By.CSS_SELECTOR, "div[class='signup-form'] input[name='email']")
        self.signUpSubmit = (By.XPATH,"//button[text()='Signup']")


    def newUserSignUp(self, name, email):
        name_field = self.wait.until(expected_conditions.visibility_of_element_located(self.signupName))
        self.highlight(name_field)
        name_field.send_keys(name)

        email_field= self.driver.find_element(*self.signupEmail)
        self.highlight(email_field)
        email_field.send_keys(email)

        submit = self.driver.find_element(*self.signUpSubmit)
        self.highlight(submit)
        submit.click()