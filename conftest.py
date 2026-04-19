import pytest
from selenium import webdriver
import random

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