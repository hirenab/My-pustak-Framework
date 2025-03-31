# Automation Testing Framework for MyPustak

## Project Overview

This project is an automated test suite designed for https://www.mypustak.com/. It includes functional tests covering core functionalities like **Login**, **Search**, and **Add to Cart**. The framework is built using `pytest` and `Selenium WebDriver`, with the goal of ensuring the website's functionality works as expected across different user scenarios.

### Key Features:
- **Automated Login**: Tests both valid and invalid login attempts.
- **Search Functionality**: Tests multiple search cases, including special characters, empty search, and regular searches.
- **Add to Cart**: Verifies that users can add books to the cart successfully.
- **Parameterized Tests**: Used for testing various inputs efficiently (e.g., different search queries).
- **Modular Design**: Page Object Model (POM) is used to keep the test code clean, maintainable, and reusable.
- **Fixtures**: `pytest` fixtures are used for WebDriver setup and teardown, ensuring a fresh browser instance for every test.

### Files and Folders

- `pages/`: Contains the Page Object Model classes for the Login, Search, and Cart functionalities.
- `locators.py`: Contains locators for the elements used across different pages.
- `tests/`: Contains all test cases. Each functionality (login, search, cart) has its own test file.
- `conftest.py`: Contains common fixtures for setup and teardown of WebDriver.
- `requirements.txt`: Lists all dependencies needed to run the tests (Selenium, WebDriver Manager, Pytest).
- `pytest.ini`: Configuration for Pytest to define settings such as markers.

## Test Cases

### 1. **Login Tests**
   - **Valid Login**: Ensures a user can log in with correct credentials.
   - **Invalid Login**: Tests login with incorrect credentials and checks for proper error messages.
   - **Empty Email/Password**: Tests login attempts with empty email and password fields.

### 2. **Search Functionality Tests**
   - **Valid Search**: Tests search functionality with valid queries like "Computer" and verifies results.
   - **Empty Search**: Ensures that searching without any input still returns results or displays a message.
   - **Special Character Search**: Verifies that searches containing special characters like `#` and `!@#$%` display an appropriate error message.

### 3. **Add to Cart Tests**
   - **Add Book to Cart**: Ensures that a user can add books to the cart and the cart is updated correctly.
   - **Cart Item Verification**: Verifies the number of items in the cart and their correct details.

## Setup Instructions

### Prerequisites:
- Python 3.8 or higher installed.
- Google Chrome or another supported browser.

### Step-by-Step Guide:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/mypustak-automation-framework.git
   cd mypustak-automation-framework
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows, use venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Tests**
   To execute the tests, run the following command:
   ```bash
   pytest --html=report.html --self-contained-html
   ```

   This command will run the tests and generate an HTML report (`report.html`) showing the results.

## Dependencies

- `selenium`: For browser automation.
- `webdriver_manager`: Automatically handles downloading and setting up WebDriver for the tests.
- `pytest`: Framework for writing and running test cases.
- `pytest-html`: Plugin to generate detailed HTML reports.

Install all dependencies via:
```bash
pip install -r requirements.txt
```

---

### Future Improvements
- **Cross-browser Testing**: Expand the test suite to run on Firefox and Edge.
- **Continuous Integration**: Integrate with CI/CD pipelines such as GitHub Actions or Jenkins.
- **Data-Driven Testing**: Implement more extensive test coverage using data-driven test cases.

