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
def registration_data():
    return{
        'name':'ИмяИмя',
        'email':'anna_lastname_44_753@ya.ru',
        'password':'123456',
        'wrong_password':'wrong_password'
        }

@pytest.fixture
def gen_data():
    num = random.randint(100, 999)
    return {
        'name': f'Anna{num}',
        'email': f'anna_lastname_{num}@yandex.ru',
        'password': f'pass{num}'
    }