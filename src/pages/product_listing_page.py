from selenium.webdriver.common.by import By

class ProductListingPage:
    def __init__(self, driver):
        self.driver = driver
        self.product_items = (By.CLASS_NAME, 'inventory_item')
        self.product_name = (By.CLASS_NAME, 'inventory_item_name')
        self.product_price = (By.CLASS_NAME, 'inventory_item_price')
        self.add_to_cart_button = (By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack')
        self.remove_from_cart_button = (By.CSS_SELECTOR, '#remove-sauce-labs-backpack')
    
    def get_all_products(self):
        return self.driver.find_elements(*self.product_items)
    
    def get_product_names(self):
        return [product.find_element(*self.product_name).text for product in self.get_all_products()]
    
    def get_product_prices(self):
        return [product.find_element(*self.product_price).text for product in self.get_all_products()]
    
    def get_add_to_cart_button(self):
        return self.driver.find_elements(*self.add_to_cart_button)
    
    def click_add_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()

    def get_remove_from_cart_button(self):
        return self.driver.find_elements(*self.remove_from_cart_button)
    
    def click_remove_from_cart(self):
        self.driver.find_element(*self.remove_from_cart_button).click()