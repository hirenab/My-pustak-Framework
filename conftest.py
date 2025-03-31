import pytest
from selenium import webdriver

@pytest.fixture
def setup_teardown():
    """Setup and teardown WebDriver session."""
    driver = webdriver.Chrome()  # Update if using another browser
    driver.maximize_window()
    driver.get("https://mypustak.com")  # Replace with actual URL
    yield driver
    driver.quit()
