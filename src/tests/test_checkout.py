import pytest
from selenium import webdriver
import os
import json
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.browser_manager import load_browser_config, get_driver, get_base_url
from common.browser_manager import login
from pages.inventory_page import InventoryPage
from pages.check_out_page import CheckoutPage
from pages.cart_page import CartPage
from selenium.webdriver.common.by import By

load_dotenv()


@pytest.fixture(scope="module",params=load_browser_config())
def driver(request):
    browser = request.param
    driver = get_driver(browser)
    driver.get(get_base_url())
    login(driver, os.getenv('USERNAME'), os.getenv('PASSWORD'))
    yield driver
    driver.quit()

def load_test_data():
    with open('test_data.json') as data_file:
        return json.load(data_file)
    
def proceed_to_checkout(cart_page, checkout_page):
    test_data = load_test_data()
    cart_page.click_shopping_cart()
    cart_page.click_checkout_button()
    checkout_page.fill_checkout_information(test_data['checkout_info']['fname'], test_data['checkout_info']['lname'], test_data['checkout_info']['postcode'])
    checkout_page.click_continue()

def test_checkout_process(driver):
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    proceed_to_checkout(cart_page, checkout_page)
    title = checkout_page.get_checkout_overview()
    assert title == "Checkout: Overview", f"Expected text to be 'Checkout: Overview' but got '{title}'"

def test_complete_purchase(driver):
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    proceed_to_checkout(cart_page, checkout_page)
    checkout_page.click_finish()
    title = checkout_page.get_checkout_complete_title()
    assert title == "Checkout: Complete!", f"Expected text to be 'Checkout: Complete!' but got '{title}'"
