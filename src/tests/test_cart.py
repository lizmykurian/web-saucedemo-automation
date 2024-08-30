import pytest
from selenium import webdriver
import json
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.browser_manager import load_browser_config, get_driver, get_base_url, login
from pages.inventory_page import InventoryPage
from pages.product_listing_page import ProductListingPage
from pages.cart_page import CartPage
from selenium.webdriver.common.by import By

# Load environment variables
load_dotenv()

# Load the test data from the json file
with open('test_data.json') as config_file:
    config_data = json.load(config_file)

# browser config and credentials for parameterization
@pytest.fixture(params=[(browser, credentials) for browser in load_browser_config() for credentials in config_data["valid_credentials"]],
                ids=[f"{credentials['username']}_{browser}" for browser in load_browser_config() for credentials in config_data["valid_credentials"]])
def driver(request):
    browser, credentials = request.param
    driver = get_driver(browser)
    driver.get(get_base_url())
    
    # Login with the credentials from dataset
    login(driver, credentials['username'], credentials['password'])
    
    yield driver
    
    driver.quit()

def test_cart_items_displayed(driver):
    product_listing_page = ProductListingPage(driver)
    cart_page = CartPage(driver)
    product_listing_page.click_add_to_cart()
    cart_page.click_shopping_cart()
    cart_items = cart_page.get_cart_items()
    assert len(cart_items) > 0, "No items in the cart."

def test_checkout_button(driver):
    cart_page = CartPage(driver)
    cart_page.click_shopping_cart()
    cart_page.click_checkout_button()
    title = cart_page.get_checkout_page_title()
    assert title == "Checkout: Your Information", f"Expected text to be 'Checkout: Your Information' but got '{title}'"
