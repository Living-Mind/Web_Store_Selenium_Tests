from selenium import webdriver

class HomePage:
    def __init__(self):
        self.driver = webdriver.Firefox()

    def homepage_url(self):
        self.driver.get("https://petstore.octoperf.com/actions/Catalog.action") 

    def goto_category(self, xpath):
        self.driver.find_element("xpath", xpath).click()