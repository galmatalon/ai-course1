from pages.base_page import BasePage


class HeaderArea(BasePage):

    def __init__(self, page):
        super().__init__(page)

    __MENU_BTN = "#react-burger-menu-btn"
    __LOGOUT_BTN = "#logout_sidebar_link"

    def logout(self):
        self.click(self.__MENU_BTN)
        self.click(self.__LOGOUT_BTN)