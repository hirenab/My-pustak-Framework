from pages.search_page import SearchPage
import pytest

@pytest.mark.parametrize("search_query, expected_result", [
    ("Harry Potter", "Harry Potter"),
    ("", ""),
])
def test_search_functionality(setup_teardown, search_query, expected_result):
    driver = setup_teardown
    search_page = SearchPage(driver)

    search_page.search_item(search_query)
    book_titles = search_page.get_search_results()

    if search_query == "Harry Potter":
        assert any(expected_result in title.text for title in book_titles), "Relevant books not found!"
    elif search_query == "":
        assert len(book_titles) > 0, "No books found when searching without input!"
    else:
        assert len(book_titles) > 0, "Unfortunately the page you are looking for has been moved or deleted"

import pytest

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
