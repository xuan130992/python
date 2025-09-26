from pagesPOM.base_page import  Base
from playwright.sync_api import expect


class partner_page(Base):

    @property
    def logo(self):
        return self.page.locator("//*[@id='logo']")

    def verify_login_success(self):
        expect(self.logo).to_be_visible()
