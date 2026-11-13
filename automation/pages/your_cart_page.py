from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.components.header_area import HeaderArea


class YourCartPage(HeaderArea, BasePage):

    def __init__(self, page:Page):
        super().__init__(page)

    __CHECKOUT_BTN = "#checkout"

    def checkout(self):
        self.click(self.__CHECKOUT_BTN)

    def remove_product(self, product_name):
        pass
