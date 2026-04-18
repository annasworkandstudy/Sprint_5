from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from lokators import Lokators_name

class TestRegistrationAccount:
    def test_successfull_registration(self, driver, registration_data, gen_data):
        driver.get('https://stellarburgers.education-services.ru/register')
        driver.find_element(*Lokators_name.INPUT_NAME).send_keys(gen_data['name'])
        driver.find_element(*Lokators_name.INPUT_EMAIL).send_keys(gen_data['email'])
        driver.find_element(*Lokators_name.INPUT_PASSWORD).send_keys(gen_data['password'])
        driver.find_element(*Lokators_name.BUTTON_REGISTRATION).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Lokators_name.BUTTON_ACCOUNT_ENTER))
        driver.find_element(*Lokators_name.INPUT_EMAIL).send_keys(gen_data['email'])
        driver.find_element(*Lokators_name.INPUT_PASSWORD).send_keys(gen_data['password'])
        driver.find_element(*Lokators_name.BUTTON_ACCOUNT_ENTER).click()
        email_value=driver.find_element(*Lokators_name.INPUT_EMAIL).get_attribute('value')
        assert email_value == gen_data['email']

    def test_uncorrect_password(self, driver, registration_data):
        driver.get('https://stellarburgers.education-services.ru/login')
        driver.find_element(*Lokators_name.INPUT_EMAIL).clear()
        driver.find_element(*Lokators_name.INPUT_PASSWORD).clear()
        driver.find_element(*Lokators_name.INPUT_EMAIL).send_keys(registration_data['email'])
        driver.find_element(*Lokators_name.INPUT_PASSWORD).send_keys(registration_data['wrong_password'])
        driver.find_element(*Lokators_name.BUTTON_ACCOUNT_ENTER).click()
        email_value=driver.find_element(*Lokators_name.INPUT_EMAIL).get_attribute('value')
        assert email_value == registration_data['email']
