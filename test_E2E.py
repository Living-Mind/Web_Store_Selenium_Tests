from selenium import webdriver
from PageObjects.HomePage import HomePage
from PageObjects.SignInPage import SignInPage
from PageObjects.OrderPage import OrderPage 
from PageObjects.CartPage import CartPage
from PageObjects.GoldfishPage import GoldfishPage
from time import sleep

def test_E2E():

    driver = webdriver.Firefox()
    driver.get("https://petstore.octoperf.com/actions/Catalog.action")

    #Homepage section
    homepage = HomePage(driver)
    homepage.click_sign_in()

    #Sign In section
    signin_page = SignInPage(driver)
    signin_page.enter_username()
    signin_page.clear_field()
    #sleep(3)
    signin_page.enter_password()
    signin_page.click_login()


    #Homepage logged in section
    homepage.enter_word_search()
    #sleep(3)
    homepage.click_search()
    homepage.click_gold_fish_product()

    #Goldfish section
    goldfish_page =  GoldfishPage(driver)
    goldfish_page.add_goldfish_product()


    #Shopping cart section    
    cart_page = CartPage(driver)
    cart_page.click_proceed()

    #Order section
    order_page = OrderPage(driver)
    order_page.click_continue()
    order_page.click_confirm()
    assert order_page.text_confirm() == "Thank you, your order has been submitted."

    driver.quit()

