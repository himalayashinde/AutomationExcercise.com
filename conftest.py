import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browserInstance():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


