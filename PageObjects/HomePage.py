from seleniumpagefactory.Pagefactory import PageFactory


class HomePage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "sign_in": ("CSS", "#MenuContent > a:nth-child(3)"),
        "username": ("ID", "WelcomeContent"),
        "search_word": ("CSS", "#SearchContent > form:nth-child(1) > input:nth-child(1)"),
        "search_button": ("CSS", "#SearchContent > form:nth-child(1) > input:nth-child(2)"),
        "gold_fish_product": ("CSS", "#Catalog > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > a:nth-child(1)"),

    }

    def click_sign_in(self):
        self.sign_in.click()

    def enter_word_search(self):
        self.search_word.set_text("gold")

    def click_search(self):
        self.search_button.click()

    def click_gold_fish_product(self):
        self.gold_fish_product.click()