from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from lokators import Lokators_name

class TestAccountEnter:
    def test_enter_account_button(self, driver, registration_data):
        driver.get('https://stellarburgers.education-services.ru')
        driver.find_element(*Lokators_name.BUTTON_ACCOUNT_ENTER_MAIN).click()
        driver.find_element(*Lokators_name.INPUT_EMAIL).send_keys(registration_data['email'])
        driver.find_element(*Lokators_name.INPUT_PASSWORD).send_keys(registration_data['password'])
        driver.find_element(*Lokators_name.BUTTON_ACCOUNT_ENTER).click()
        order_button = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Lokators_name.BUTTON_ORDER))
        assert order_button.text == 'Оформить заказ'

    def test_enter_personal_account_main_page(self, driver, registration_data):
        driver.get('https://stellarburgers.education-services.ru/')
        driver.find_element(*Lokators_name.BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(*Lokators_name.INPUT_EMAIL).send_keys(registration_data['email'])
        driver.find_element(*Lokators_name.INPUT_PASSWORD).send_keys(registration_data['password'])
        driver.find_element(*Lokators_name.BUTTON_ACCOUNT_ENTER).click()
        order_button = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Lokators_name.BUTTON_ORDER))
        assert order_button.text == 'Оформить заказ'

    def test_enter_from_registration(self, driver, registration_data):
        driver.get('https://stellarburgers.education-services.ru/register')
        driver.find_element(*Lokators_name.BUTTON_ENTER_ACCOUNT_REGISTRATION).click()
        driver.find_element(*Lokators_name.INPUT_EMAIL).send_keys(registration_data['email'])
        driver.find_element(*Lokators_name.INPUT_PASSWORD).send_keys(registration_data['password'])
        driver.find_element(*Lokators_name.BUTTON_ACCOUNT_ENTER).click()
        order_button = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Lokators_name.BUTTON_ORDER))
        assert order_button.text == 'Оформить заказ'
    
    def test_enter_from_recovery(self, driver, registration_data):
        driver.get('https://stellarburgers.education-services.ru/forgot-password')
        driver.find_element(*Lokators_name.BUTTON_ENTER_ACCOUNT_REGISTRATION).click()
        driver.find_element(*Lokators_name.INPUT_EMAIL).send_keys(registration_data['email'])
        driver.find_element(*Lokators_name.INPUT_PASSWORD).send_keys(registration_data['password'])
        driver.find_element(*Lokators_name.BUTTON_ACCOUNT_ENTER).click()
        order_button = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Lokators_name.BUTTON_ORDER))
        assert order_button.text == 'Оформить заказ'