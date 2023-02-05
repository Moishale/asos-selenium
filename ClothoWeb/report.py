from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class ClothoWebReport:
    def __init__(self, boxes_section_elements: WebElement):
        self.boxes_section_elements = boxes_section_elements
        self.product_boxes = self.pull_product_boxes()

    def pull_product_boxes(self):
        return self.boxes_section_elements.find_elements(
            By.CSS_SELECTOR, 'article.productTile_hwDN1'
        )

    def pull_product_box_attributes(self):
        collection = []
        for product_box in self.product_boxes:
            product_title = product_box.find_element(
                By.CSS_SELECTOR, 'div.overflowFade_zrNEl'
            ).get_attribute('innerText')
            product_price = product_box.find_element(
                By.CLASS_NAME, 'span.price_CMH3V'
            ).get_attribute('innerText')

            collection.append(
                [product_title, product_price]
            )
        return collection
