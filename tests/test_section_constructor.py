from lokators import Lokators_name

class TestConstructor:
    def test_constructor_sauces(self, driver):
        driver.get('https://stellarburgers.education-services.ru')
        driver.find_element(*Lokators_name.SAUCES).click()
        current_tab = driver.find_element(*Lokators_name.SAUCES).get_attribute("class")
        assert "tab_tab_type_current" in current_tab

    def test_constructor_bun(self, driver):
        driver.get('https://stellarburgers.education-services.ru')
        driver.find_element(*Lokators_name.SAUCES).click()
        driver.find_element(*Lokators_name.BUN).click()
        current_tab = driver.find_element(*Lokators_name.BUN).get_attribute("class")
        assert "tab_tab_type_current" in current_tab

    def test_constructor_fillings(self, driver):
        driver.get('https://stellarburgers.education-services.ru')
        driver.find_element(*Lokators_name.FILLINGS).click()
        current_tab = driver.find_element(*Lokators_name.FILLINGS).get_attribute("class")
        assert "tab_tab_type_current" in current_tab
