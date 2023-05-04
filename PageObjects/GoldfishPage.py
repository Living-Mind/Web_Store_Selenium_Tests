from seleniumpagefactory.Pagefactory import PageFactory

class GoldfishPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver


    locators = {

       "add_goldfish": ("CSS", "#Catalog > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(5) > a:nth-child(1)"),


    }


    def add_goldfish_product(self):
        self.add_goldfish.click()



    