from PageObjects.HomePage import HomePage
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import time
import pytest


def test_fish_left_category_redirect():

    home_page = HomePage()
    home_page.homepage_url()
    home_page.goto_category("/html/body/div[2]/div[2]/div[1]/div/a[1]")
    #home_page.driver.find_element()
    assert home_page.driver.find_element("xpath", "/html/body/div[2]/div[2]/h2").text == "Fish", "Category not the same"
    time.sleep(5)
    home_page.driver.quit()


test_fish_left_category_redirect()