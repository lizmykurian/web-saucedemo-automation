from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_items = (By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[1]')
        self.shopping_cart = (By.CSS_SELECTOR, '#shopping_cart_container')
        self.checkout_page_title = (By.XPATH, '//*[@id="header_container"]/div[2]/span')
        self.checkout_button = (By.CSS_SELECTOR,'#checkout')
    
    def get_cart_items(self):
        return self.driver.find_elements(*self.cart_items)
    
    def click_shopping_cart(self):
        self.driver.find_element(*self.shopping_cart).click()
    
    def get_checkout_page_title(self):  
       return self.driver.find_element(*self.checkout_page_title).text

    def click_checkout_button(self):
        self.driver.find_element(*self.checkout_button).click()
