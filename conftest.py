import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='firefox',
                     help="Choose browser: chrome, firefox or edge")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: en or fr")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        # Объявление инициализации для браузера Google Chrome
        print("\nstart chrome browser for test..")

        # It's work in Chrome with Windows, Linux and macOS
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

        browser = webdriver.Chrome(chrome_options=options)
    elif browser_name == "firefox":
        # Объявление инициализации для браузера Mozilla Firefox
        print("\nstart firefox browser for test..")
        #browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

        # It's work in Chrome with Windows, Linux and macOS
        options = webdriver.FirefoxOptions()
        #options.add_argument("--start-maximized")
        options.set_preference("intl.accept_languages", user_language)

        browser = webdriver.Firefox(options=options)
        browser.maximize_window()
    elif browser_name == "edge":
        # Объявление инициализации для браузера Microsoft Edge
        print("\nstart edge browser for test..")

        # It's work in Chrome with Windows, Linux and macOS
        options = webdriver.EdgeOptions()
        options.add_argument("--start-maximized")
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

        browser = webdriver.Edge(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
