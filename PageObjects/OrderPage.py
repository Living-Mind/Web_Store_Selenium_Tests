from seleniumpagefactory.Pagefactory import PageFactory

class OrderPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver


    locators = {

        "continue_button": ("CSS", "#Catalog > form:nth-child(1) > input:nth-child(2)"),
        "confirm_button": ("CSS", ".Button"),
        "conformation_text": ("CSS", ".messages > li:nth-child(1)")
    }

    def click_continue(self):
        self.continue_button.click()

    def click_confirm(self):
        self.confirm_button.click()

    def text_confirm(self):
        return self.conformation_text.get_text()


