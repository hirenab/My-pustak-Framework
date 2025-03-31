class Urls:
    LOGIN_URL = "https://www.mypustak.com/"

class LocateById:
    LOGIN_BUTTON_ID = "loginBtn"
    SNACKBAR_ID = "notistack-snackbar"

class LocateByClass:
    POPUP_LOGIN_CLASS = "WLoginNavbar_loginButton__M7mhW"

class LocateByXpath:
    SEARCH_BAR_XPATH = '//input[@id="gsearch"]'  
    SEARCH_BUTTON_XPATH = '//button[@id="searchId"]'  
    RESULT_TITLES_XPATH = '(//div[contains(@class, "search-page")]//div[contains(@class, "BookCard")])[1]'  
    ERROR_MESSAGE_XPATH = '//*[contains(@class, "title-error")]'
    EMAIL_INPUT_XPATH = "//label[contains(text(),'Enter your email address')]/..//input"
    PASSWORD_INPUT_XPATH = '//div[@class="WLoginNavbar_loginDialogRightDiv__x6Kbk"]/form/div/div[2]/div/input'
    EMAIL_ERROR_XPATH = '//div[@class="WLoginNavbar_loginDialogRightDiv__x6Kbk"]/form/div/div[1]/div/p'
    ADD_TO_CART_XPATH = "(//div[contains(@class,'search-page')]//button[contains(., 'Add to Cart')])[1]"
    ADD_TO_CART_POPUP_BTN_XPATH = "(//div[@aria-describedby='alert-dialog-slide-description']//button[contains(., 'Add to Cart')])[1]"
    ADD_TO_CART_FINAL_XPATH = "(//button[contains(@class, 'Product_productAddtoCarddiv__hWTQk')])[1]"
    BOOK_ADDED_TO_CART_XPATH = "//span[contains(text(),'Book added to cart!')]"
    CART_ICON = "//span[@id='cartIcon']"
    LOGIN_BTN = '//button[@id="loginBtn"]/span'
    ADD_BUTTON = '//*[@id="yousaved"]/div/div/button[2]'
    QUANTITY = '//*[@id="yousaved"]/div/div/span[1]'
