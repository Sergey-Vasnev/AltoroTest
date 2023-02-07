from selenium.webdriver.common.by import By
class Locator():
    locType = By.NAME
    SEARCH_FIELD_YOUR_NAME = (locType, "name")  # creates locator for Your Name field
    SEARCH_FIELD_YOUR_EMAIL = (locType, "email_addr")  # creates locator for Your Email Address field
    SEARCH_SUBJECT = (locType, "subject")  # creates locator for YSubject field
    SEARCH_COMMENTS = (locType, "comments")  # creates locator for Question/Comment field
    SUBMIT_BUTTON = (locType, "submit")  # creates locator for submit button