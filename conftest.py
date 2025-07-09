import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browserName",action="store",default="chrome",help="By Default Chrome selected as commandline argument not provided"
    )


@pytest.fixture(scope="function")
def browserInstance(request):
    browserName= request.config.getoption("browserName")
    if browserName =="chrome":
        driver = webdriver.Chrome()

    elif browserName == "edge":
        driver = webdriver.Edge()

    else:
        driver = webdriver.Firefox()

    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://automationexercise.com/")
    yield driver
    driver.close()


