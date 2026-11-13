from playwright.sync_api import Page


class BasePage:

    def __init__(self, page:Page):
        self.__page = page

    @property
    def page(self):
        return self.__page

    def click(self, locator):
        self._highlight_element(locator, "pink")
        self.__page.locator(locator).click()

    def fill_text(self, locator, text):
        self._highlight_element(locator, "yellow")
        self.__page.locator(locator).fill(text)

    def select_option(self, locator, sort_option):
        self._highlight_element(locator, "yellow")
        self.page.locator(locator).select_option(value=sort_option)

    def get_text(self, locator):
        self._highlight_element(locator, "orange")
        return self.page.locator(locator).inner_text()

    # Highlights a web element temporarily by changing its background color and box shadow.
    # This is useful for debugging or visual tracking during automated test runs.
    # Parameters:
    #   locator (str): The selector used to locate the element on the page.
    #   color (str): The background color to use for highlighting (default is yellow).
    def _highlight_element(self, locator: str, color: str = "yellow"):
        element = self.__page.locator(locator)
        element.evaluate(f"""
            (el) => {{
                const origShadow = el.style.boxShadow;
                const origBackground = el.style.backgroundColor;

                el.style.boxShadow = '0 0 10px 4px rgba(0, 150, 255, 0.7)';
                el.style.backgroundColor = '{color}';

                setTimeout(() => {{
                    el.style.boxShadow = origShadow;
                    el.style.backgroundColor = origBackground;
                }}, 300);
            }}
        """)