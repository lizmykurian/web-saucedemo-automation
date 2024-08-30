from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.page_url = 'https://www.saucedemo.com/inventory.html'
        self.inventory = (By.ID, 'inventory_container')
        self.filter = (By.CLASS_NAME, 'product_sort_container')
        self.low_to_high = (By.XPATH, "//option[text()='Price (low to high)']")
        self.high_to_low = (By.XPATH, "//option[text()='Price (high to low)']")
        self.item_price = (By.CLASS_NAME, 'inventory_item_price')
    
    def is_open(self):
        return self.driver.current_url == self.page_url
    def get_inventory(self):
        return self.driver.find_elements(*self.inventory)
    def get_page_title(self):
        return self.driver.title
    
    def sort_by_price_low_to_high(self):
       self.driver.find_element(*self.filter).click()
       self.driver.find_element(*self.low_to_high).click()
    
    def sort_by_price_high_to_low(self):
        self.driver.find_element(*self.filter).click()
        self.driver.find_element(*self.high_to_low).click()
    
    def get_product_prices(self):
        price_elements = self.driver.find_elements(*self.item_price)
        return [float(price.text[1:]) for price in price_elements]


 