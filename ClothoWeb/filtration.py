from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class ClothoWebFiltration:
    def __init__(self, driver, genders):
        self.driver = driver
        self.genders = genders

    def apply_gender_change(self):
        self._click_gender_filter_button()
        gender_options = self._get_gender_options()
        self._select_genders(gender_options)
        self._close_filter_box()

    def _click_gender_filter_button(self):
        self.driver.find_element(By.CSS_SELECTOR, "#plp > div > div.container_TILjd > div > div > div.horizontalRefinements_qVf1h > ul > li:nth-child(3) > div > button").click()

    def _get_gender_options(self):
        gender_options = self.driver.find_elements(By.CLASS_NAME, 'value_hLBn8')
        return gender_options

    def _select_genders(self, gender_options):
        if 'men' in self.genders:
            gender_options[0].click()
        if 'women' in self.genders:
            gender_options[1].click()
        if 'unisex' in self.genders:
            gender_options[2].click()

    def _close_filter_box(self):
        self.driver.find_element(By.CSS_SELECTOR, "#plp > div > div.container_TILjd > div > div > div.horizontalRefinements_qVf1h > ul > li:nth-child(3) > div > button").send_keys(Keys.ESCAPE)
    
    def sort_price_lowest_first(self):
        sorting_box = self.driver.find_element(By.CSS_SELECTOR, '#plp > div > div.container_TILjd > div > div > div.horizontalRefinements_qVf1h > ul > li:nth-child(1) > div > button')
        sorting_box.click()

        element = self.driver.find_element(By.CSS_SELECTOR, '#plp_web_sort_price_low_to_high')
        element.click()
        
        sorting_box.send_keys(Keys.ESCAPE)
        