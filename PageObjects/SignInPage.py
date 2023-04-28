from seleniumpagefactory.Pagefactory import PageFactory

class SignInPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "username_input": ("NAME", "username"),
        "password_input": ("NAME", "password"),
        "login_button": ("CSS", "#Catalog > form:nth-child(1) > input:nth-child(3)")
    }

    def enter_username(self):
        self.username_input.set_text("test")

    def enter_password(self):
        self.password_input.set_text("test")

    def click_login(self):
        self.login_button.click()

    def clear_field(self):
        self.password_input.clear()