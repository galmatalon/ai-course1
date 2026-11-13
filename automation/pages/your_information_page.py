from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.components.header_area import HeaderArea


class YourInformationPage(HeaderArea, BasePage):

    def __init__(self, page:Page):
        super().__init__(page)

    __FIRST_NAME_FIELD = "#first-name"
    __LAST_NAME_FIELD = "#last-name"
    __ZIP_FIELD = "#postal-code"
    __CONTINUE_BTN = "#continue"

    def fill_info(self, first_name, last_name, zip):
        self.fill_text(self.__FIRST_NAME_FIELD,first_name)
        self.fill_text(self.__LAST_NAME_FIELD,last_name)
        self.fill_text(self.__ZIP_FIELD,zip)
        self.click(self.__CONTINUE_BTN)
