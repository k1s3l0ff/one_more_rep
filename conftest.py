import pytest
from selenium.webdriver import Chrome


@pytest.fixture(scope='module')
def browser():
    driver = Chrome()
    yield driver
    driver.quit()
