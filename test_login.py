from selenium import webdriver
from PageObjects.SignInPage import SignInPage
from time import sleep


def test_login():
    driver = webdriver.Firefox()
    driver.get("https://petstore.octoperf.com/actions/Account.action?signonForm=")

    signin_page = SignInPage(driver)



    signin_page.enter_username()

    sleep(5)
    

    signin_page.clear_field() 
    sleep(5)
    signin_page.enter_password()

    
    sleep(5)
    signin_page.click_login()
    
    sleep(5)
    #driver.quit()
