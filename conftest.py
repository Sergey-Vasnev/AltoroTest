import pytest
from BrowserFactory import Driver
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="edge",
                     help="Choose browser: chrome or firefox")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    print(browser_name)
    browser = Driver.chooseDriver(request.config.getoption("browser_name"))
    print(hex(id(browser)))
    yield browser
    print("\nquit browser..")
    browser.quit()