import ClothoWeb.constants as const
from ClothoWeb.filtration import ClothoWebFiltration
from ClothoWeb.report import ClothoWebReport

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from prettytable import PrettyTable


class ClothoWeb(webdriver.Chrome):
    def __init__(self, teardown=False):
        self.service = Service(ChromeDriverManager().install())
        self.teardown = teardown
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option(
            'excludeSwitches', ['enable-logging'])
        super(ClothoWeb, self).__init__(service=self.service,
                                        options=self.options, service_log_path='NUL')
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def select_product_to_search(self, product):
        self.search_field_locator = (By.CSS_SELECTOR, '#chrome-search')
        self.submit_button_locator = (By.CLASS_NAME, '_1KRfEms')

        self._search(product)

    def _search(self, product):
        search_field = self.find_element(*self.search_field_locator)
        search_field.send_keys(product)

        submit_button = self.find_element(*self.submit_button_locator)
        submit_button.click()

    def apply_filtrations(self):
        filtration = ClothoWebFiltration(self, const.GENDERS)
        filtration.apply_gender_change()
        filtration.sort_price_lowest_first()

    def report_results(self):
        product_boxes = self.find_element(
            By.CSS_SELECTOR, 'section.listingPage_HfNlp'
        )

        report = ClothoWebReport(product_boxes)
        table = PrettyTable(
            field_names=['Product Title', 'Product Price']
        )
        table.add_rows(report.pull_product_box_attributes())
        print(table)

