from lokators import Lokators_name
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data_reg import DataReg

class TestEntrance:
    #Тест на проверку перехода в личный кабинет при условии авторизованного пользователя
    def test_entrance_account_authorized(self, driver):
        driver.get('https://stellarburgers.education-services.ru/')
        driver.find_element(*Lokators_name.BUTTON_ACCOUNT_ENTER_MAIN).click()
        driver.find_element(*Lokators_name.INPUT_EMAIL).send_keys(DataReg.email)
        driver.find_element(*Lokators_name.INPUT_PASSWORD).send_keys(DataReg.password)
        driver.find_element(*Lokators_name.BUTTON_ACCOUNT_ENTER).click()
        driver.find_element(*Lokators_name.BUTTON_PERSONAL_ACCOUNT).click()
        cancel_btn = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Lokators_name.BUTTON_CANCEL))
        assert cancel_btn.text == 'Отмена'

    #Тест на проверку перехода в личный кабинет при неавторизованном пользователе
    def test_entrance_not_authorized(self, driver):
        driver.get('https://stellarburgers.education-services.ru/')
        driver.find_element(*Lokators_name.BUTTON_PERSONAL_ACCOUNT).click()
        login_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Lokators_name.BUTTON_ACCOUNT_ENTER))
        assert login_button.text == 'Войти'

    
