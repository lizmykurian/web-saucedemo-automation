from selenium.webdriver.common.by import By

class ProductDetailsPage:
    def __init__(self, driver):
        self.driver = driver
      #  self.product_name = (By.CLASS_NAME, 'inventory_details_name')
        self.product_name = (By.CSS_SELECTOR,'#item_4_title_link > div')
        self.product_description = (By.XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]/div[2]')
        self.product_price = (By.XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]/div[3]')
        self.add_to_cart_button = (By.CSS_SELECTOR, '#add-to-cart')
        self.remove_from_cart_button = (By.CSS_SELECTOR, '#remove')

    def get_product_name(self):
        return self.driver.find_element(*self.product_name).text
 
    def get_product_description(self):
        self.driver.find_element(*self.product_name).click() 
        return self.driver.find_element(*self.product_description)
    
    def get_product_price(self):
        return self.driver.find_element(*self.product_price)
    
    def get_add_to_cart(self):
        return self.driver.find_element(*self.add_to_cart_button).text
    
    def click_add_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()

    def get_remove_from_cart(self):
        return self.driver.find_element(*self.remove_from_cart_button).text
    
    def click_remove_from_cart(self):
        self.driver.find_element(*self.remove_from_cart_button).click()

