from selenium.webdriver.common.by import By
from utils.browserutils import BrowserUtils


class HomePage(BrowserUtils):
    """Page object for the Automation Exercise home page."""

    def __init__(self, driver):
        """
        Initialize the HomePage object.
        Args:
            driver (selenium.webdriver): The Selenium WebDriver instance.
        """
        self.driver = driver
        self.signup_login_link = (By.XPATH, "//a[text()=' Signup / Login']")

    def click_signup_login(self) -> None:
        """
        Clicks the 'Signup / Login' link on the home page.
        """
        click_signup = self.driver.find_element(*self.signup_login_link)
        self.highlight(click_signup)
        click_signup.click()
