import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                 help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    lang = request.config.getoption("language")
    
    if lang is not None:
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': lang})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language parameter is not provided")
    yield browser
    print("\nquit browser..")
    browser.quit()
