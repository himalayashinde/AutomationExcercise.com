class BrowserUtils:

    def __init__(self, driver):
        self.driver =driver

    def getTitle(self):
        return self.driver.title

    def highlight(self, element, duration=2):
        # Highlight with red border using JavaScript
        original_style = element.get_attribute('style')
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                                   element, "border: 2px solid red; background: yellow;")
        import time
        time.sleep(duration)
        # Revert back
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                                   element, original_style)
