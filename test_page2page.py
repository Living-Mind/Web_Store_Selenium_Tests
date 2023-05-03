from selenium import webdriver
from PageObjects.HomePage import HomePage
from PageObjects.SignInPage import SignInPage
from time import sleep

def test_page2page():

    driver =  webdriver.Firefox()
    driver.get("https://petstore.octoperf.com/actions/Catalog.action")

    homepage = HomePage(driver)

    homepage.click_sign_in()

    signin_page = SignInPage(driver)

    signin_page.click_register()

    sleep(5)

    driver.quit()

