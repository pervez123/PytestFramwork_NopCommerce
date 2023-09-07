import os
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    browser_name = request.config.getoption("--browser_name")
    if browser_name.lower() == 'chrome':
        driver = webdriver.Chrome(options=chrome_options)
    elif browser_name.lower() == 'firefox':
        driver = webdriver.Firefox()
    elif browser_name.lower() == 'ie':
        driver = webdriver.Ie()
    driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
    driver.implicitly_wait(10)
    # driver.delete_all_cookies()
    driver.find_element(By.ID, "Email").clear()
    driver.find_element(By.ID, "Email").send_keys("admin@yourstore.com")
    driver.find_element(By.ID, "Password").clear()
    driver.find_element(By.ID, "Password").send_keys("admin")
    driver.find_element(By.XPATH, "//button[text()= 'Log in']").click()
    request.cls.driver = driver
    yield
    time.sleep(5)
    driver.close()


def pytest_html_report_title(report):
    report.title = "Nopcommerce Test Report!"


def _pytest_configure_(config):
    config.metadata['Project Name'] = 'nop Commerce'
    config.metadata['Module Name'] = 'Customers'
    config.meta['Tester'] = 'Pervez'


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


# Modify the _capture_screenshot function to save the screenshots in the "Reports" directory
def _capture_screenshot(name):
    screenshot_path = os.path.join("Reports", name)
    driver.get_screenshot_as_file(screenshot_path)


# @pytest.fixture()
# def login(request):
#     driver = request.cls.driver
#     driver.find_element(By.ID, "Email").clear()
#     driver.find_element(By.ID, "Email").send_keys("admin@yourstore.com")
#     driver.find_element(By.ID, "Password").clear()
#     driver.find_element(By.ID, "Password").send_keys("admin")
#     driver.find_element(By.XPATH, "//button[text()= 'Log in']").click()
