import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox");
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: en or fr");

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name");
    user_language = request.config.getoption("language");
    browser = None;
    if browser_name == "chrome":
        print("\nstart chrome browser for test..");
        browser = webdriver.Chrome();

        # It's work in Chrome with Windows, Linux and macOS
        options = webdriver.ChromeOptions();
        options.add_argument("--start-maximized");
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language});

        browser = webdriver.Chrome();
        browser = webdriver.Chrome(chrome_options=options);
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..");
        browser = webdriver.Firefox();

        # It's work in Chrome with Windows, Linux and macOS
        options = webdriver.FirefoxOptions();
        options.add_argument("--start-maximized");
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language});

        browser = webdriver.Firefox();
        browser = webdriver.Firefox(firefox_binary=options);
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox");
    yield browser
    print("\nquit browser..");
    browser.quit();