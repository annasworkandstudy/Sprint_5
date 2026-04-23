from lokators import Lokators_name
from selenium.webdriver.support import expected_conditions as EC
from data_reg import DataReg

class TestEntrance:
    #Тест на проверку перехода в личный кабинет при условии авторизованного пользователя
    def test_entrance_account_authorized(self, driver, wait):
        driver.get('https://stellarburgers.education-services.ru/')
        driver.find_element(*Lokators_name.BUTTON_ACCOUNT_ENTER_MAIN).click()
        driver.find_element(*Lokators_name.INPUT_EMAIL).send_keys(DataReg.email)
        driver.find_element(*Lokators_name.INPUT_PASSWORD).send_keys(DataReg.password)
        driver.find_element(*Lokators_name.BUTTON_ACCOUNT_ENTER).click()
        driver.find_element(*Lokators_name.BUTTON_PERSONAL_ACCOUNT).click()
        assert wait.until(EC.visibility_of_element_located(Lokators_name.BUTTON_CANCEL))

    #Тест на проверку перехода в личный кабинет при неавторизованном пользователе
    def test_entrance_not_authorized(self, driver, wait):
        driver.get('https://stellarburgers.education-services.ru/')
        driver.find_element(*Lokators_name.BUTTON_PERSONAL_ACCOUNT).click()
        assert wait.until(EC.visibility_of_element_located(Lokators_name.BUTTON_ACCOUNT_ENTER))

    
