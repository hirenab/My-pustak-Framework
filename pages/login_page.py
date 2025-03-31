from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Increased timeout

    def click_login_button(self):
        """Clicks the login button to open the login popup."""
        try:
            login_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='undefined icon']")))
            login_button.click()
        except StaleElementReferenceException:
            login_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='undefined icon']")))
            login_button.click()  # Retry clicking

    def enter_email(self, email):
        """Enters the email in the input field."""
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.MuiInputBase-input"))).clear()
        email_input = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.MuiInputBase-input")))
        email_input.send_keys(email)

    def click_proceed(self):
        """Clicks the 'Proceed' button."""
        proceed_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.WLoginNavbar_loginButton__M7mhW")))
        proceed_button.click()

    def enter_password(self, password):
        """Enters the password."""
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='password']"))).clear()
        password_input = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='password']")))
        password_input.send_keys(password)
    
    def perform_login(self, email, password):
        """Complete login process with given email and password."""
        self.click_login_button()
        self.enter_email(email)
        self.click_proceed()
        self.enter_password(password)
        self.click_login()

    def click_login(self):
        """Clicks the final login button."""
        login_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.WLoginNavbar_loginButton__M7mhW")))
        login_button.click()

    def get_error_message(self):
        """Fetches the error message displayed on login failure."""
        try:
            error_message = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, '//div[@class="WLoginNavbar_loginDialogRightDiv__x6Kbk"]/form/div/div[1]/div/p'))
            )
            return error_message.text
        except :
            return None  # Return None if no error appears

    