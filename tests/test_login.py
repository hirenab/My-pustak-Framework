import pytest
from pages.login_page import LoginPage
from data.test_data import VALID_EMAIL, VALID_PASSWORD, INVALID_EMAIL, INVALID_PASSWORD, EMPTY_EMAIL, EMPTY_PASSWORD
from selenium.common.exceptions import StaleElementReferenceException


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
import data.test_data


@pytest.mark.login
def test_login_valid(setup_teardown):
    """TC01: Login with valid credentials"""
    driver = setup_teardown
    login_page = LoginPage(driver)

    try:
        login_page.click_login_button()
        login_page.enter_email(VALID_EMAIL)
        login_page.click_proceed()
        login_page.enter_password(VALID_PASSWORD)
        login_page.click_login()
    except StaleElementReferenceException:
        login_page.click_login_button()  # Retry

    # assert "Dashboard" in driver.title, "Login failed!"

@pytest.mark.login
def test_login_invalid_credentials(setup_teardown):
    """TC02: Login with invalid email & password"""
    driver = setup_teardown
    login_page = LoginPage(driver)

    login_page.click_login_button()
    login_page.enter_email(INVALID_EMAIL)
    login_page.click_proceed()

    error_text = login_page.get_error_message()
    assert "Enter valid email" in error_text, "Expected error message not found!"
   

@pytest.mark.login
def test_login_empty_fields(setup_teardown):
    """TC03: Login with empty email & password fields"""
    driver = setup_teardown
    login_page = LoginPage(driver)

    login_page.click_login_button()
    login_page.enter_email("")
    login_page.click_proceed()

    error_text = login_page.get_error_message()
    assert "Enter valid email" in error_text, "Expected error message not found!"

@pytest.mark.login
def test_login_case_sensitivity(setup_teardown):
    """TC04: Check email case sensitivity"""
    driver = setup_teardown
    login_page = LoginPage(driver)

    login_page.click_login_button()
    login_page.enter_email(VALID_EMAIL.upper())  # Uppercase email
    login_page.click_proceed()
    login_page.enter_password(VALID_PASSWORD)
    login_page.click_login()

@pytest.mark.login
def test_login_invalid_email_format(setup_teardown):
    """TC05: Login with invalid email format"""
    driver = setup_teardown
    login_page = LoginPage(driver)

    login_page.click_login_button()
    login_page.enter_email("invalidemail.com")  # Invalid email format
    login_page.click_proceed()

    error_text = login_page.get_error_message()
    assert error_text is not None, "Expected error message not found!"

@pytest.mark.login
def test_login_invalid_password(setup_teardown):
    driver = setup_teardown
    login_page = LoginPage(driver)

    # Step 1: Perform login with valid email and invalid password
    login_page.click_login_button()
    login_page.enter_email(data.test_data.VALID_EMAIL)  # Use a valid email
    login_page.click_proceed()
    # login_page.wait_for_password_input()
    login_page.enter_password(data.test_data.INVALID_EMAIL)  # Use an invalid password
    login_page.click_proceed()

    # Step 2: Wait for the error snackbar to appear
    try:
        snackbar = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "notistack-snackbar"))
        )
        error_message = snackbar.text
    except:
        pytest.fail("Snackbar did not appear. Login error message not displayed.")

    # Step 3: Assert the error message
    expected_message = "Entered email or password is incorrect"  # Update this if the actual message is different
    assert error_message == expected_message, f"Expected '{expected_message}', but got '{error_message}'"

