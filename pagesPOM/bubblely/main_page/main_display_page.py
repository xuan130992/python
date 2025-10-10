from playwright.sync_api import Page, ElementHandle
from Util.common_locator import CommonLocator
class main_display_page(Page):
    def   __init__(self, page: Page):
        self.page = page
    def open_mainpage(self):
        self.page.goto("https://bubblyz-qa.onstove.com/en/showcase")


