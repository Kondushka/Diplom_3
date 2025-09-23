from seletools.actions import drag_and_drop
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    def find_element_and_click(self, locator):
        element = self.find_element(locator)
        return element.click()
        
    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))   

    def wait_clickable_and_click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        return element.click()  

    def input_keys(self, locator, text):
        element = self.wait_visible(locator)
        return element.send_keys(text)

    def wait_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def drag_and_drop_element(self, locator_from, locator_to):
        source = self.find_element(locator_from)
        target = self.find_element(locator_to)
        return drag_and_drop(self.driver, source, target)
    
    def wait_until_element_is_invisible(self, locator):
        return WebDriverWait(self.driver, 20).until_not(EC.visibility_of_element_located(locator))