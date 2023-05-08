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
        "dogs_category": ("CSS", "#SidebarContent > a:nth-child(4)"),
        "breed_bulldog": ("CSS", "#Catalog > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2)"),
        "breed_poodle": ("CSS", "#Catalog > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2)"),
        "breed_dalmation": ("CSS", "#Catalog > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2)"),
        "breed_golden_retriever": ("CSS", "#Catalog > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(2)"),
        "breed_labrador_retriever": ("CSS", "#Catalog > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(6) > td:nth-child(2)"),
        "breed_chihuahua": ("CSS", "#Catalog > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(7) > td:nth-child(2)"),
        "button_return_main_menu": ("CSS", "#BackLink")

    }

    def click_sign_in(self):
        self.sign_in.click()

    def enter_word_search(self):
        self.search_word.set_text("gold")

    def click_search(self):
        self.search_button.click()

    def click_gold_fish_product(self):
        self.gold_fish_product.click()

    def click_dogs_category(self):
        self.dogs_category.click()

    def text_bulldog(self):
        return self.breed_bulldog.get_text()

    def text_poodel(self):
        return self.breed_poodle.get_text()

    def text_dalmation(self):
        return self.breed_dalmation.get_text()

    def text_golden_retriever(self):
        return self.breed_golden_retriever.get_text()

    def text_labrador_retriever(self):
        return self.breed_labrador_retriever.get_text()

    def text_chichuahua(self):
        return self.breed_chihuahua.get_text()

    def click_return_menu(self):
        self.button_return_main_menu.click()