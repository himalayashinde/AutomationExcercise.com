import pytest
import json

from selenium.webdriver.common.by import By

from pages.login import LoginPage

# Load test data
with open("test_data/testdata.json") as f:
    data = json.load(f)["data"][0]
    username = data["username"]
    password = data["password"]


def test_e2e(browserInstance):
    driver = browserInstance

    driver.find_element(By.XPATH, "//a[text()=' Signup / Login']").click()


    loginPage = LoginPage(driver)
    print(loginPage.getTitle())
    loginPage.newUserSignUp("Himalaya","himalaya@yammer.com")

