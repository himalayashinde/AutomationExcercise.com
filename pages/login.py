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
        self.wait.until(expected_conditions.visibility_of_element_located(self.signupName)).send_keys(name)
        self.driver.find_element(*self.signupEmail).send_keys(email)
        self.driver.find_element(*self.signUpSubmit).click()