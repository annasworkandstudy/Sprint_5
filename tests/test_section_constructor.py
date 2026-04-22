from lokators import Lokators_name
from selenium.webdriver.support import expected_conditions

class TestConstructor:
    def test_constructor_sauces(self, driver, wait):
        driver.get('https://stellarburgers.education-services.ru')
        wait.until(expected_conditions.element_to_be_clickable(Lokators_name.SAUCES)).click()
        wait.until(expected_conditions.text_to_be_present_in_element_attribute(Lokators_name.SAUCES, "class", "tab_tab_type_current"))
        current_tab = driver.find_element(*Lokators_name.SAUCES).get_attribute("class")
        assert "tab_tab_type_current" in current_tab

    def test_constructor_bun(self, driver, wait):
        driver.get('https://stellarburgers.education-services.ru')
        wait.until(expected_conditions.element_to_be_clickable(Lokators_name.SAUCES)).click()
        wait.until(expected_conditions.element_to_be_clickable(Lokators_name.BUN)).click()
        wait.until(expected_conditions.text_to_be_present_in_element_attribute(Lokators_name.BUN, "class", "tab_tab_type_current"))
        current_tab = driver.find_element(*Lokators_name.BUN).get_attribute("class")
        assert "tab_tab_type_current" in current_tab

    def test_constructor_fillings(self, driver, wait):
        driver.get('https://stellarburgers.education-services.ru')
        wait.until(expected_conditions.element_to_be_clickable(Lokators_name.FILLINGS)).click()
        wait.until(expected_conditions.text_to_be_present_in_element_attribute(Lokators_name.FILLINGS, "class", "tab_tab_type_current"))
        current_tab = driver.find_element(*Lokators_name.FILLINGS).get_attribute("class")
        assert "tab_tab_type_current" in current_tab
