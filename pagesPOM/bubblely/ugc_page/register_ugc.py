from playwright.sync_api import Page, ElementHandle
from playwright.sync_api import Playwright
from pagesPOM.base_page import Base
class register_Ugc(Base):
    def __init__(self, page:Page):
        self.page=page
        self.iframe=page.frame_locator("#iframe-BLZ00000005001")

    @property
    def mod_type(self)-> ElementHandle:
        return self.iframe.locator()
    @property
    def mod_type_selected(self)-> ElementHandle:
        return self.iframe.locator()
    @property
    def package_version(self)-> ElementHandle:
        return self.iframe.locator()
    @property
    def visibility(self)-> ElementHandle:
        return self.iframe.locator()
    @property
    def set_country(self)-> ElementHandle:
        return self.iframe.locator()
    @property
    def select_country(self)-> ElementHandle:
        return self.iframe.locator()
    @property
    def register_country_btn(self)-> ElementHandle:
        return self.iframe.locator()
    @property
    def ingame_display_order(self)-> ElementHandle:
        return self.iframe.locator()
    @property
    def english_title(self)-> ElementHandle:
        return self.iframe.locator()
    @property
    def english_description(self)-> ElementHandle:
        return self.iframe.locator()
    @property
    def genre_settings(self)-> ElementHandle:
        return self.iframe.locator()
    @property
    def genre_selected(self)-> ElementHandle:
        return self.iframe.locator()
    @property
    def add_screenshot(self)-> ElementHandle:
        return self.iframe.locator()
    @property
    def upload_screenshot(self)-> ElementHandle:
        return self.iframe.locator()
    @property
    def android_file_upload(self)-> ElementHandle:
        return self.iframe.locator()
    @property
    def ios_file_upload(self)-> ElementHandle:
        return self.iframe.locator()
    @property
    def windowns_file_upload(self)-> ElementHandle:
        return self.iframe.locator()
    @property
    def server_file_upload(self)-> ElementHandle:
        return self.iframe.locator()
    @property
    def register_btn(self)-> ElementHandle:
        return self.iframe.locator()
    @property
    def confirm_btn(self)-> ElementHandle:
        return self.iframe.locator()

    def register_ugc(self, backage,display_order,eng_title,eng_description):
        self.mod_type.click()
        self.mod_type_selected.click()
        self.package_version.fill(backage)
        self.set_country.click()
        self.select_country.click()
        self.register_country_btn.click()
        self.ingame_display_order.fill(display_order)
        self.english_title.fill(eng_title)
        self.english_description.click(eng_description)
        self.genre_settings.click()
        self.genre_selected.click()
        self.register_btn.click()
        self.confirm_btn.click()






