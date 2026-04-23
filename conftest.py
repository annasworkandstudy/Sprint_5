import pytest
from selenium import webdriver
import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def gen_data():
    num = random.randint(100, 999)
    return {
        'name': f'Anna{num}',
        'email': f'anna_lastname_{num}@yandex.ru',
        'password': f'pass{num}'
    }

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)