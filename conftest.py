import pytest
from selenium import webdriver

@pytest.fixture(scope="session") #creating fixture
def browser():
    driver = webdriver.Firefox() #sets Firefox as default webdriver
    yield driver
    driver.quit() #quit driver after test session