from playwright.sync_api import Page, ElementHandle, Locator

from Util.common_functions import CommonFunctions
from pagesPOM.base_page import Base


class registerbanner_page(Base):
    def __init__(self, page: Page):
        self.page = page
        self.iframe = page.frame_locator("#iframe-BLZ00000001004")
        self.common_functions = CommonFunctions(page)

    @property
    def title_input(self) -> ElementHandle:
        return self.iframe.locator('//*[@id="component-title"]')

    @property
    def display_options(self) -> ElementHandle:
        return self.iframe.locator('(//*[@name="display_true"])[1]')

    @property
    def display_period(self) -> ElementHandle:
        return self.iframe.locator('//*[@id="component-display-period"]')

    @property
    def display_order(self) -> ElementHandle:
        return self.iframe.locator('//*[@id="component-displayOrder"]')

    @property
    def banner_btn(self) -> ElementHandle:
        return self.iframe.locator('//*[@class="p-button p-component p-button-primary text-14"]')
    @property
    def banner_type(self) -> ElementHandle:
        return self.iframe.locator('//*[contains(text(),"Image Type")]')


    @property
    def main_title_input(self) -> ElementHandle:
        return self.iframe.locator('//*[@id="mainTitle-en-0"]')

    @property
    def sub_title_input(self) -> ElementHandle:
        return self.iframe.locator('//*[@id="subTitle-en-0"]')

    @property
    def upload_button_PC(self) -> ElementHandle:
        return self.iframe.locator('(//*[contains(text(),"Upload")])[1]')

    @property
    def upload_button_mobile(self) -> ElementHandle:
        return self.iframe.locator('(//*[contains(text(),"Upload")])[2]')

    @property
    def link(self) -> ElementHandle:
        return self.iframe.locator('//*[@id="link"]')

    @property
    def link_input(self) -> ElementHandle:
        return self.iframe.locator('//*[@class="p-inputtext p-component w-350 text-14"]')

    @property
    def register_btn(self) -> ElementHandle:
        return self.iframe.locator('//*[contains(text(),"Register") and @class="p-button-label"]')

    @property
    def register_complete_btn(self) -> ElementHandle:
        return self.iframe.locator('//*[contains(text(),"Confirm") and @class="p-button-label"]')

    def register_banner_component(self, title, display_order, link_value):
        self.title_input.fill(title)
        self.display_options.check()
        self.display_order.fill(display_order)
        self.banner_btn.click()
        self.main_title_input.fill(title)
        #self.upload_button_PC.click()
        self.link_input.fill(link_value)

    def register_hero_banner_component(self, title,sub_title, display_order, link_value):
        self.title_input.fill(title)
        self.display_options.check()
        self.display_order.fill(display_order)
        self.banner_btn.click()
        self.banner_type.click()
        self.main_title_input.fill(title)
        self.sub_title_input.fill(sub_title)
        self.link_input.fill(link_value)

    def register_btn_act(self):
        self.register_btn.click()
        self.register_complete_btn.click()







