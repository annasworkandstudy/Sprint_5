from selenium.webdriver.support import expected_conditions
from lokators import Lokators_name
from data_reg import DataReg

class TestAccountEnter:
    def test_enter_account_button(self, driver, wait):
        driver.get('https://stellarburgers.education-services.ru')
        driver.find_element(*Lokators_name.BUTTON_ACCOUNT_ENTER_MAIN).click()
        driver.find_element(*Lokators_name.INPUT_EMAIL).send_keys(DataReg.email)
        driver.find_element(*Lokators_name.INPUT_PASSWORD).send_keys(DataReg.password)
        driver.find_element(*Lokators_name.BUTTON_ACCOUNT_ENTER).click()
        assert wait.until(expected_conditions.visibility_of_element_located(Lokators_name.BUTTON_ORDER))

    def test_enter_personal_account_main_page(self, driver, wait):
        driver.get('https://stellarburgers.education-services.ru/')
        driver.find_element(*Lokators_name.BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(*Lokators_name.INPUT_EMAIL).send_keys(DataReg.email)
        driver.find_element(*Lokators_name.INPUT_PASSWORD).send_keys(DataReg.password)
        driver.find_element(*Lokators_name.BUTTON_ACCOUNT_ENTER).click()
        assert wait.until(expected_conditions.visibility_of_element_located(Lokators_name.BUTTON_ORDER))

    def test_enter_from_registration(self, driver, wait):
        driver.get('https://stellarburgers.education-services.ru/register')
        driver.find_element(*Lokators_name.BUTTON_ENTER_ACCOUNT_REGISTRATION).click()
        driver.find_element(*Lokators_name.INPUT_EMAIL).send_keys(DataReg.email)
        driver.find_element(*Lokators_name.INPUT_PASSWORD).send_keys(DataReg.password)
        driver.find_element(*Lokators_name.BUTTON_ACCOUNT_ENTER).click()
        assert wait.until(expected_conditions.visibility_of_element_located(Lokators_name.BUTTON_ORDER))
    
    def test_enter_from_recovery(self, driver, wait):
        driver.get('https://stellarburgers.education-services.ru/forgot-password')
        driver.find_element(*Lokators_name.BUTTON_ENTER_ACCOUNT_REGISTRATION).click()
        driver.find_element(*Lokators_name.INPUT_EMAIL).send_keys(DataReg.email)
        driver.find_element(*Lokators_name.INPUT_PASSWORD).send_keys(DataReg.password)
        driver.find_element(*Lokators_name.BUTTON_ACCOUNT_ENTER).click()
        assert wait.until(expected_conditions.visibility_of_element_located(Lokators_name.BUTTON_ORDER))