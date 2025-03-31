from data import test_data
from locators import LocateByXpath
from pages.login_page import LoginPage  # Ensure correct import
from pages.search_page import SearchPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_add_to_cart_and_open_cart(setup_teardown):

    """Test to search for a book, add it to the cart, and open the cart page."""
    driver = setup_teardown

    # Step 1: Initialize LoginPage and perform login
    login_page = LoginPage(driver)  # Only pass driver to __init__()
    login_page.perform_login(test_data.VALID_EMAIL, test_data.VALID_PASSWORD)
    
    time.sleep(2)  # Small delay to allow login completion
    
    # Step 2: Perform search
    search_page = SearchPage(driver)
    search_page.search_item("Harry Potter")  # Example search query
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, LocateByXpath.RESULT_TITLES_XPATH))
    )
    
    book_titles = search_page.get_search_results()
    
    # Step 3: Click "Add to Cart"
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, LocateByXpath.ADD_TO_CART_XPATH))
    )
    # driver.execute_script("arguments[0].scrollIntoView();", add_to_cart_button)
    time.sleep(1)  # Ensure the button is interactable
    add_to_cart_button.click()
    
    time.sleep(2)
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, LocateByXpath.ADD_TO_CART_POPUP_BTN_XPATH))
    )

    time.sleep(1)  # Ensure the button is interactable
    add_to_cart_button.click()
    
    # # Step 4: Click the cart icon in the header
    # cart_icon = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, LocateByXpath.CART_ICON))
    # )
    # cart_icon.click()
