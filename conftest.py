import pytest
from selenium import webdriver

LOGIN_URL = "https://www.mypustak.com/"

@pytest.fixture(scope='function')
def setup_teardown():
    """Fixture to set up and tear down WebDriver."""
    driver = webdriver.Chrome()
    driver.get(LOGIN_URL)
    driver.maximize_window()
    yield driver
    driver.quit()
