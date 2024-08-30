import pytest
from selenium import webdriver
import json
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.browser_manager import load_browser_config, get_driver, get_base_url
from common.browser_manager import login
from pages.inventory_page import InventoryPage
from pages.product_listing_page import ProductListingPage
from selenium.webdriver.common.by import By

load_dotenv()



with open('test_data.json') as config_file:
    config_data = json.load(config_file)


@pytest.fixture(params=[(browser, credentials) for browser in load_browser_config() for credentials in config_data["valid_credentials"]],
                ids=[f"{credentials['username']}_{browser}" for browser in load_browser_config() for credentials in config_data["valid_credentials"]])
def driver(request):
    browser, credentials = request.param
    driver = get_driver(browser)
    driver.get(get_base_url())
    
    login(driver, credentials['username'], credentials['password'])
    
    yield driver
    
    driver.quit()

def test_product_listing_page_loads(driver):
    product_listing_page = ProductListingPage(driver)
    products = product_listing_page.get_all_products()
    assert len(products) > 0, "No products found on the product listing page."

def test_product_names_and_prices_displayed(driver):
    product_listing_page = ProductListingPage(driver)
    product_names = product_listing_page.get_product_names()
    product_prices = product_listing_page.get_product_prices()
    
    assert all(product_names), "Some product names are missing."
    assert all(product_prices), "Some product prices are missing."

def test_add_product_to_cart(driver):
    product_listing_page = ProductListingPage(driver)
    assert product_listing_page.get_add_to_cart_button(),"Add to cart action is unsuccessfull."


def test_remove_product_from_cart(driver):
    product_listing_page = ProductListingPage(driver)
    product_listing_page.click_add_to_cart()
    assert product_listing_page.get_remove_from_cart_button(),"Remove action is unsuccessfull."