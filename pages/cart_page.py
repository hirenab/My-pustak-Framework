from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LocateByXpath

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def get_cart_items(self):
        """Returns the list of books present in the cart."""
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, LocateByXpath.BOOK_ADDED_TO_CART_XPATH))
        )
