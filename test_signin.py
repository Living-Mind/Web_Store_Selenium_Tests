from selenium import webdriver
from PageObjects.HomePage import HomePage

def test_singin():
    driver = webdriver.Firefox()
    driver.get("https://petstore.octoperf.com/actions/Catalog.action")


    homepage = HomePage(driver)

    homepage.click_sign_in()
    driver.quit()