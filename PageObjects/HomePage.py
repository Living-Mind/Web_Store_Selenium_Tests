from seleniumpagefactory.Pagefactory import PageFactory


class HomePage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "sign_in": ("CSS", "#MenuContent > a:nth-child(3)"),
        "username": ("ID", "WelcomeContent")
    }

    def click_sign_in(self):
        self.sign_in.click()
