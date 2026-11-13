from playwright.sync_api import Page

from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page:Page):
        super().__init__(page)

    __USER_NAME_FIELD = "#user-name"
    __PASSWORD_FIELD = "#password"
    __LOGIN_BTN = "#login-button"
    __ERROR_MSG_LABEL = "[data-test='error']"

    def login(self, username, password):
        self.fill_text(self.__USER_NAME_FIELD, username)
        self.fill_text(self.__PASSWORD_FIELD, password)
        self.click(self.__LOGIN_BTN)

    def get_error_message(self):
        return self.get_text(self.__ERROR_MSG_LABEL)


