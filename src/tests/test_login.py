import pytest
import json
from common.browser_manager import load_browser_config, get_driver, get_base_url
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def load_test_data():
    with open('test_data.json') as data_file:
        return json.load(data_file)

@pytest.fixture(params=load_browser_config())
def driver(request):
    browser = request.param
    driver = get_driver(browser)
    driver.get(get_base_url())
    yield driver
    driver.quit()

def test_login_valid_credentials(driver):
    test_data = load_test_data()
    
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    
    login_page.login(test_data['valid_credentials']['username'], test_data['valid_credentials']['password'])
    
    assert inventory_page.is_open()

def test_login_invalid_credentials(driver):
    test_data = load_test_data()
    login_page = LoginPage(driver)
    login_page.login(test_data['invalid_credentials']['username'], test_data['invalid_credentials']['password'])
    # Get the error message and perform assertions
    error_message = login_page.get_error_message()
    assert "Epic sadface: Username and password do not match any user in this service" in error_message


def test_login_emptyfields_credentials(driver): 
    login_page = LoginPage(driver)
    login_page.login('', '')
    error_message = login_page.get_error_message()
    assert "Epic sadface: Username is required" in error_message
