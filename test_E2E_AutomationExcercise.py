import pytest
import json

from selenium.webdriver.common.by import By

from pages.homepage import HomePage
from pages.login import LoginPage
from pages.signup import SignUp

# Load test data
with open("test_data/testdata.json") as f:
    data = json.load(f)["data"][0]
    username = data["username"]
    password = data["password"]


def test_e2e(browserInstance):
    driver = browserInstance
    #     Test Case 1: Register User
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    # 3. Verify that home page is visible successfully
    homepage =HomePage(driver)
    homepage.getTitle()
    # 4. Click on 'Signup / Login' button
    homepage.click_signup_login()

    # 5. Verify 'New User Signup!' is visible
    # 6. Enter name and email address
    # 7. Click 'Signup' button

    loginPage = LoginPage(driver)
    print(loginPage.getTitle())
    loginPage.newUserSignUp("Himalaya","himalaya@yammer.com")


    sign_up=SignUp(driver)

    # 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
    assert sign_up.validate_Label_Enter_Account_Info(), "'Enter Account Information' is not visible"

# 9. Fill details: Title, Name, Email, Password, Date of birth
# 10. Select checkbox 'Sign up for our newsletter!'
# 11. Select checkbox 'Receive special offers from our partners!'
# 12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
# 13. Click 'Create Account button'
# 14. Verify that 'ACCOUNT CREATED!' is visible
# 15. Click 'Continue' button
# 16. Verify that 'Logged in as username' is visible
# 17. Click 'Delete Account' button
# 18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
