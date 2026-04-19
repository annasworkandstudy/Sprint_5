from lokators import Lokators_name
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data_reg import DataReg

class TestEnterToConstructor:

    def test_enter_to_constructor(self, driver):
        driver.get('https://stellarburgers.education-services.ru/')
        driver.find_element(*Lokators_name.BUTTON_ACCOUNT_ENTER_MAIN).click()
        driver.find_element(*Lokators_name.INPUT_EMAIL).send_keys(DataReg.email)
        driver.find_element(*Lokators_name.INPUT_PASSWORD).send_keys(DataReg.password)
        driver.find_element(*Lokators_name.BUTTON_ACCOUNT_ENTER).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Lokators_name.BUTTON_ORDER))
        driver.find_element(*Lokators_name.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Lokators_name.BUTTON_CONSTRUCTOR)).click()
        header = driver.find_element(*Lokators_name.HEADER_BURGER)
        assert header.text == 'Соберите бургер'