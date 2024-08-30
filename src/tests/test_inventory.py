import pytest
from selenium import webdriver
import json
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.browser_manager import load_browser_config, get_driver, get_base_url
from common.browser_manager import login
from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By

load_dotenv()


# Load the test data from the json file
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

def test_inventory_page_loads(driver):
    inventory_page = InventoryPage(driver)
    title = inventory_page.get_page_title()
    assert "Swag Labs" in title, "Page title does not contain 'Swag Labs'."

def test_sort_by_price_low_to_high(driver):
    inventory_page = InventoryPage(driver)
    inventory_page.sort_by_price_low_to_high()
    
    prices = inventory_page.get_product_prices()
    assert prices == sorted(prices), "Prices are not sorted from low to high."

def test_sort_by_price_high_to_low(driver):
    inventory_page = InventoryPage(driver)
    inventory_page.sort_by_price_high_to_low()
    
    prices = inventory_page.get_product_prices()
    assert prices == sorted(prices, reverse=True), "Prices are not sorted from high to low."
