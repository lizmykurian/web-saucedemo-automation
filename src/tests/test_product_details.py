import pytest
from selenium import webdriver
import json
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.browser_manager import load_browser_config, get_driver, get_base_url
from common.browser_manager import login
from pages.inventory_page import InventoryPage
from pages.product_details_page import ProductDetailsPage
from selenium.webdriver.common.by import By

load_dotenv()


# Load the test data from the config file
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


def test_product_details_page_loads(driver):
    product_details_page = ProductDetailsPage(driver)
    title = product_details_page.get_product_name()
    assert "Sauce Labs Backpack" in title, f"Expected text to be 'Expected Text' but got '{title}'"
    assert product_details_page.get_product_description(), "Product description is not displayed."
    assert product_details_page.get_product_price(), "Product price is not displayed."

def test_add_product_to_cart(driver):
    product_details_page = ProductDetailsPage(driver)
    assert product_details_page.get_add_to_cart(),"Add to cart action is unsuccessfull."


def test_remove_product_from_cart(driver):
    product_details_page = ProductDetailsPage(driver)
  #  product_details_page.click_remove_from_cart()
    product_details_page.click_add_to_cart()
    assert product_details_page.get_remove_from_cart(),"Remove action is unsuccessfull."