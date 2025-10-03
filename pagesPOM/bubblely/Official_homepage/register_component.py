from playwright.sync_api import ElementHandle, Page,expect
from pagesPOM.base_page import Base



class register_component(Base):
    def __init__(self, page:Page):
        self.page = page
        self.iframe=page.frame_locator("#iframe-BLZ00000001004")
        self.iframe_cp=page.frame_locator("#iframe-BLZ00000001004")
    @property
    def bubblely_menu(self)->ElementHandle:
        return self.page.locator('//*[contains(text(),"Bubblelyz")]')

    @property
    def official_homepage_menu(self)-> ElementHandle:
        return self.page.locator('//*[contains(text(), "Official Homepage Management")]')

    @property
    def page_component(self)->ElementHandle:
        return self.page.locator('//*[contains(text(), "Page Component Management")]')

    @property
    def select_country(self)->ElementHandle:
        return self.iframe.locator("//*[@id='country']")

    @property
    def input_country(self) -> ElementHandle:
            return self.iframe.locator('//*[@class="p-inputtext p-component p-select-filter text-14"]')

    @property
    def select_country_details(self)->ElementHandle:
        return self.iframe.locator('//*[contains(text(),"Republic of Korea (used)")]')



    @property
    def register_btn(self)->ElementHandle:
        return self.iframe.locator('//*[contains(text(),"Register Component")]')

    @property
    def search_components_btn(self)->ElementHandle:
        return self.iframe.locator('//*[@class="p-button-icon i-mdi:magnify text-20"]')


    @property
    def register_component_option(self)->ElementHandle:
        return self.iframe.locator('//*[contains(text(),"Please select the type of component to register.")]')

    @property
    def select_feature_mod(self)->ElementHandle:
        return self.iframe.locator('//*[contains(text(),"Featured Mod")]')

    @property
    def register_form(self)->ElementHandle:
        return self.iframe.locator('//*[contains(text(),"Basic Information")]')


    def register_component_act(self,country):
        self.bubblely_menu.click()
        self.official_homepage_menu.click()
        self.page_component.click()
        self.select_country.click()
        self.input_country.fill(country)
        self.select_country_details.click()
        self.register_btn.click()
        self.select_feature_mod.click()



    def verify_register_btn(self):
        expect(self.register_form).to_be_visible()


