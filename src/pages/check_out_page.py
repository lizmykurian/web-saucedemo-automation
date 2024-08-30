from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.ID, 'first-name')
        self.last_name = (By.ID, 'last-name')
        self.postal_code = (By.ID, 'postal-code')
        self.continue_button = (By.ID, 'continue')
        self.finish_button = (By.ID, 'finish')
        self.checkout_overview = (By.XPATH,'//*[@id="header_container"]/div[2]/span')
        self.checkout_complete_title = (By.XPATH,'//*[@id="header_container"]/div[2]/span')
        
    
    def fill_checkout_information(self, first_name, last_name, postal_code):
        self.driver.find_element(*self.first_name).send_keys(first_name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.postal_code).send_keys(postal_code)
    
    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()
    
    def click_finish(self):
        self.driver.find_element(*self.finish_button).click()

    def get_checkout_overview(self):
        return self.driver.find_element(*self.checkout_overview).text
    
    def get_checkout_complete_title(self):
        return self.driver.find_element(*self.checkout_complete_title).text
