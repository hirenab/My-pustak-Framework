from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import SEARCH_BAR_XPATH, SEARCH_BUTTON_XPATH, RESULT_TITLES_XPATH, ERROR_MESSAGE_XPATH

class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    def search_item(self, search_query):
        search_bar = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, SEARCH_BAR_XPATH)))
        search_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, SEARCH_BUTTON_XPATH)))
        
        search_bar.clear()
        search_bar.send_keys(search_query)
        search_button.click()

    def get_search_results(self):
        return self.driver.find_elements(By.XPATH, RESULT_TITLES_XPATH)
    
    def get_error_message(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, ERROR_MESSAGE_XPATH))).text
