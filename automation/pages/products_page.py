from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.components.header_area import HeaderArea


class ProductsPage(HeaderArea, BasePage):

    def __init__(self, page:Page):
        super().__init__(page)

    __CART_BTN = ".shopping_cart_link"
    __SORT_DD = ".product_sort_container"


    def open_cart(self):
        self.click(self.__CART_BTN)

    def sort(self, sort_option):
        self.select_option(self.__SORT_DD, sort_option)

    def add_to_cart(self, product_name):
        area_list = self.page.locator(".inventory_item")
        for i in range(area_list.count()):
            title_label = area_list.nth(i).locator(".inventory_item_name")
            title_text = title_label.inner_text()
            if title_text == product_name:
                add_to_cart_btn = area_list.nth(i).locator(".btn_primary.btn_inventory")
                add_to_cart_btn.click()
                break

