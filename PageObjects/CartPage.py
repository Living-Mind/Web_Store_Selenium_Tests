from seleniumpagefactory.Pagefactory import PageFactory

class CartPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver


    locators = {

        "proceed_checkout": ("CSS", "a.Button:nth-child(3)"),

    }

    def click_proceed(self):
        self.proceed_checkout.click()
