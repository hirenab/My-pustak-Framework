from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import SNACKBAR_ID

CORRECT_EMAIL = "hiren@gmail.com"
CORRECT_PASSWORD = "Hiren@123"
INCORRECT_PASSWORD = "982374"
INCORRECT_EMAIL = "^%#$^@!@gmail..com"

def test_login_valid(setup_teardown):
    driver = setup_teardown
    login_page = LoginPage(driver)
    login_page.perform_login(CORRECT_EMAIL, CORRECT_PASSWORD)

    login_text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//button[@id="loginBtn"]/span'))
    ).text
    assert login_text == "Login was unsuccessful!"

def test_login_invalid_password(setup_teardown):
    driver = setup_teardown
    login_page = LoginPage(driver)
    login_page.perform_login(CORRECT_EMAIL, INCORRECT_PASSWORD)

    error_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, SNACKBAR_ID))
    ).text
    assert "Entered email or password is incorrect" in error_message, "Incorrect password error not displayed!"
