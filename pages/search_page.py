from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LocateByXpath

class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    def search_item(self, search_query):
        search_bar = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, LocateByXpath.SEARCH_BAR_XPATH)))
        search_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, LocateByXpath.SEARCH_BUTTON_XPATH)))
        
        search_bar.clear()
        search_bar.send_keys(search_query)
        search_button.click()

    def get_search_results(self):
        return self.driver.find_elements(By.XPATH, LocateByXpath.RESULT_TITLES_XPATH)
    
    def get_error_message(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, LocateByXpath.ERROR_MESSAGE_XPATH))).text
