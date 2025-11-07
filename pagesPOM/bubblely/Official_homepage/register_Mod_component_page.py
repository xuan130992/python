import uuid
from xml.sax.xmlreader import Locator


from playwright.sync_api import Page, ElementHandle,expect
from pagesPOM.base_page import Base
from playwright.sync_api import Locator




class register_Mod_component(Base):

    def __init__(self, page:Page):
        self.page = page
        self.iframe=page.frame_locator("#iframe-BLZ00000001004")

    @property
    def title_input(self)-> ElementHandle:
        return self.iframe.locator('//*[@id="component-title"]')

    @property
    def display_options(self)-> ElementHandle:
        return self.iframe.locator('(//*[@name="display_true"])[1]')

    @property
    def display_period(self)-> ElementHandle:
        return self.iframe.locator('//*[@id="component-display-period"]')

    @property
    def display_order(self)-> ElementHandle:
        return self.iframe.locator('//*[@id="component-displayOrder"]')

    @property
    def use_title_options(self)-> ElementHandle:
        return self.iframe.locator('(//*[@name="display_true"])[2]')

    @property
    def en_language_component_title(self)-> ElementHandle:
        return self.iframe.locator('//*[@id="component-title-en"]')

    @property
    def set_aggregation_period(self)-> ElementHandle:
        return self.iframe.locator('//*[contains(text(),"Entire")]')

    @property
    def mod_register_btn(self)-> ElementHandle:
        return self.iframe.locator('//*[@class="p-button p-component text-14"]')

    @property
    def mod_type_btn(self)-> ElementHandle:
        return self.iframe.locator('//*[@id="modType"]')


    @property
    def over_lay(self)-> Locator:
        return self.iframe.locator('//*[@class="p-select-overlay p-component"]')

    @property
    def mod_type_select(self)-> Locator:
        return self.iframe.locator('//span[text()="Official MOD"]')

    @property
    def search_mod_btn(self)-> ElementHandle:
        return self.iframe.locator('//*[@class="p-button-icon i-mdi:magnify text-20"]')

    @property
    def mod_checkbox(self)-> ElementHandle:
        return self.iframe.locator('(//*[@class="p-checkbox-input"])[3]')

    @property
    def registe_mod_btn(self)-> ElementHandle:
        return self.iframe.locator('(//*[@class="p-button p-component text-14"])[2]')

    @property
    def register_scs_confirm(self)-> ElementHandle:
        return self.iframe.locator('//*[contains(text(),"Confirm") and @class="p-button-label"]')

    @property
    def register_btn(self)-> ElementHandle:
        return self.iframe.locator('//*[contains(text(),"Register") and @class="p-button-label"]')

    @property
    def register_complete_btn(self)-> ElementHandle:
        return self.iframe.locator('//*[contains(text(),"Confirm") and @class="p-button-label"]')




    def register_feature_component(self,title,display_order,EN_title) -> None:
        self.title_input.fill(title)
        self.display_options.check()
        self.display_order.fill(display_order)
        self.use_title_options.click()
        self.en_language_component_title.fill(EN_title)
        self.mod_register_btn.click()
        self.mod_type_btn.click()

        #self.mod_type_select.wait_for(state="visible", timeout=5000)
        self.mod_type_select.click()
        self.search_mod_btn.click()
        self.mod_checkbox.click()
        self.registe_mod_btn.click()
        self.register_scs_confirm.click()
        self.register_btn.click()
        self.register_complete_btn.click()

    def register_ranking_component(self,title,display_order,En_title) -> None:
        self.title_input.fill(title)
        self.display_options.check()
        self.display_order.fill(display_order)
        self.en_language_component_title.fill(En_title)
        self.set_aggregation_period.click()
        self.mod_register_btn.click()
        self.mod_type_btn.click()
        self.mod_type_select.click()
        self.search_mod_btn.click()
        self.mod_checkbox.click()
        self.registe_mod_btn.click()
        self.register_scs_confirm.click()
        self.register_btn.click()
        self.register_complete_btn.click()






