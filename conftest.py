import pytest
from playwright.sync_api import sync_playwright

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chromium', help='Browser to use: chromium, firefox, webkit')
    parser.addoption('--headed', action='store_true', default=False, help='Run tests with UI visible')

@pytest.fixture(scope='session')
def playwright_instance():
    pw = sync_playwright().start()
    yield pw
    pw.stop()

@pytest.fixture(scope='session')
def browser(playwright_instance, request):
    browser_name = request.config.getoption('--browser')
    headed = request.config.getoption('--headed')
    headless = not headed
    browser = getattr(playwright_instance, browser_name).launch(headless=headless)
    yield browser
    browser.close()

@pytest.fixture(scope='function')
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
