from PageObjects.HomePage import HomePage
from selenium import webdriver
import pytest
import time


def test_fish_top_category_redirect():

    home_page = HomePage()
    home_page.homepage_url()
    home_page.goto_category("/html/body/div[1]/div[4]/a[1]")
    assert home_page.driver.find_element("xpath", "/html/body/div[2]/div[2]/h2").text == "Fish", "Category name not the same"
    home_page.driver.quit()
