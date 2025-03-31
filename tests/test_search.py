from pages.search_page import SearchPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.mark.parametrize("search_query, expected_result", [
    ("Harry Potter", "Harry Potter"),
    ("", ""),
])
def test_search_functionality(setup_teardown, search_query, expected_result):
    driver = setup_teardown
    search_page = SearchPage(driver)

    search_page.search_item(search_query)

    # Wait for search results to appear
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '/html/body/main/div[3]/div/div/div/div[2]/div[2]/div[5]/div/div/div/div/div[1]/div[1]/div/div/div/div[3]/h2[1]'))  # Check if this is correct
    )  

    book_titles = search_page.get_search_results()
    if search_query:
        assert any(expected_result in title.text for title in book_titles), f"Relevant books not found for '{search_query}'!"
    else:
        assert len(book_titles) > 0, "No books found when searching without input!"


@pytest.mark.parametrize("search_query, expected_behavior", [("!@#$%^&*()_+", "404 Error !")])
def test_special_character_search(setup_teardown, search_query, expected_behavior):
    driver = setup_teardown
    search_page = SearchPage(driver)

    search_page.search_item(search_query)
    
    try:
        error_message = search_page.get_error_message()
        assert expected_behavior in error_message, f"Unexpected error displayed: {error_message}"
    except:
        book_titles = search_page.get_search_results()
        assert book_titles, f"No books found for special character search: {search_query}"
