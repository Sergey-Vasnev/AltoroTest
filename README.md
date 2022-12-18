# AltoroTest
Automated testing of Feedback form from Altoro Mutual

This program automates 3 tests for Feedback form on Altoro Mutual website (*http://testfire.net/feedback.jsp*)

I'm going to use selenium amd pytest libraries. You could install them via terminal
```
pip install pytest
pip install selenium
```

or PyCharm Python Packages
_____
Firstly, we create pytest reserved conftest.py file for fixtures where we are going to implement initialization for WebDriver. 
We implement a function named — browser, mark it with the decorator @pytest.fixture and pass the scope parameter with the "session" value. This means that this fixture function will be executed only 1 time per test session.
```pytnon
import pytest
from selenium import webdriver

@pytest.fixture(scope="session") #creating fixture
def browser():
    driver = webdriver.Firefox() #sets Firefox as default webdriver
    yield driver
    driver.quit()
```

In the browser() function we describe the commands that will be executed before the tests start. In this function we initialize webdriver and set it to be the Firefox driver. Through the yield construction we devide our function into two parts: before and after tests. In the after tests part we call for quit() function which quits current session and kills the webdriver.
