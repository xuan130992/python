from symtable import Class

from playwright.sync_api import Page,expect

class partner_page:
    def __init__(self,page:Page):
        self.app_logo =page.locator("//*[@id='logo']")

    def verify_logo(self,page:Page):
        expect(self.app_logo).to_be_visible()
