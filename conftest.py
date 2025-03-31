import pytest
from selenium import webdriver

@pytest.fixture
def setup_teardown():
    """Setup and teardown WebDriver session."""
    driver = webdriver.Chrome()  # Update if using another browser
    webdriver.options.add_argument("--headless")  # Run in headless mode
    webdriver.options.add_argument("--no-sandbox")
    webdriver.options.add_argument("--disable-dev-shm-usage")
    driver.maximize_window()
    driver.get("https://mypustak.com")  # Replace with actual URL
    yield driver
    driver.quit()
