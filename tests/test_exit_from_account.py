from lokators import Lokators_name
from selenium.webdriver.support import expected_conditions as EC
from data_reg import DataReg

class TestExitAccount:

    def test_exit_from_account(self, driver, wait):
        driver.get('https://stellarburgers.education-services.ru/login')
        driver.find_element(*Lokators_name.INPUT_EMAIL).send_keys(DataReg.email)
        driver.find_element(*Lokators_name.INPUT_PASSWORD).send_keys(DataReg.password)
        driver.find_element(*Lokators_name.BUTTON_ACCOUNT_ENTER).click()
        wait.until(EC.visibility_of_element_located(Lokators_name.BUTTON_ORDER))
        driver.find_element(*Lokators_name.BUTTON_PERSONAL_ACCOUNT).click()
        exit_button = wait.until(EC.element_to_be_clickable(Lokators_name.BUTTON_EXIT))
        exit_button.click()
        assert wait.until(EC.visibility_of_element_located(Lokators_name.BUTTON_ACCOUNT_ENTER))
