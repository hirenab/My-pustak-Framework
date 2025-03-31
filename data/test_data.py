import random
import string

# This is used for new user registration
unique_id = ''.join(random.choices(string.ascii_letters, k=2))
enter_new_email = f"user_{unique_id}@gmail.com"
enter_mobile_no = "9879879879"
enter_password = "test@000"


# Test Data
VALID_EMAIL = "hiren@gmail.com"
VALID_PASSWORD = "Hiren@123"

INVALID_EMAIL = "wronguser"
INVALID_PASSWORD = "WrongPassword123"



EMPTY_EMAIL = ""
EMPTY_PASSWORD = ""


# URL
url = "https://www.mypustak.com/"


#search your BOOK on header
search_book_name = "Harry Potter"


#product name to add in wishlist
book_name1 = "Book Of The Dead"