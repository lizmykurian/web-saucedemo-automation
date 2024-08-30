import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from dotenv import load_dotenv
from selenium.webdriver.common.by import By

# Load environment variables from .env file
load_dotenv()

def get_driver(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    
    return driver

def load_browser_config():
    browsers = os.getenv('BROWSERS', 'chrome,firefox').split(',')
    return browsers

def get_base_url():
    return os.getenv('BASE_URL', 'https://www.saucedemo.com/')

def login(driver, username, password):
    driver.find_element(By.ID, 'user-name').send_keys(username)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID, 'login-button').click()

