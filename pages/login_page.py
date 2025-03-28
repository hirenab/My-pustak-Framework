from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LOGIN_BUTTON_ID, EMAIL_INPUT_XPATH, PASSWORD_INPUT_XPATH, POPUP_LOGIN_CLASS

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def perform_login(self, email, password):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, LOGIN_BUTTON_ID))).click()
        
        if email:
            email_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, EMAIL_INPUT_XPATH)))
            email_input.clear()
            email_input.send_keys(email)

        if password:
            password_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, PASSWORD_INPUT_XPATH)))
            password_input.clear()
            password_input.send_keys(password)

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, POPUP_LOGIN_CLASS))).click()
