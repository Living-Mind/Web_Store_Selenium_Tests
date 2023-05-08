from selenium import webdriver
from PageObjects.HomePage import HomePage
from time import sleep

def test_dog_breeds_names():
    driver = webdriver.Firefox()
    driver.get("https://petstore.octoperf.com/actions/Catalog.action")

    homepage = HomePage(driver)
    homepage.click_dogs_category()
    sleep(3)
    assert homepage.text_bulldog() == "Bulldog"
    assert homepage.text_poodel() == "Poodle"
    assert homepage.text_dalmation() == "Dalmation"
    assert homepage.text_golden_retriever() == "Golden Retriever"
    assert homepage.text_labrador_retriever() == "Labrador Retriever"
    assert homepage.text_chichuahua() == "Chihuahua"
    homepage.click_return_menu()
    sleep(3)

    driver.quit()

    