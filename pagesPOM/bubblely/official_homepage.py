from playwright.sync_api import ElementHandle, Page
from pagesPOM.base_page import Base



class official_homepage(Base):
    @property
    def bubblely_menu(self)->ElementHandle:
        return self.page.locator('(//*[@class="bubblely-menu"])')

    @property
    def official_homepage_menu(self)-> ElementHandle:
        return self.page.locator('(//*[@class="official-homepage-menu"])[1]')

    @property
    def page_component(self)->ElementHandle:
        return self.page.locator('(//*[@class="page-component"])')

    @property
    def select_country(self)->ElementHandle:
        return self.page.locator('(//*[@class="select-country"])')

    @property
    def select_country_details(self)->ElementHandle:
        return self.page.locator('(//*[@class="select-country-details"])')

    @property
    def register_btn(self)->ElementHandle:
        return self.page.locator('(//*[@class="register-btn"])')

    @property
    def search_components_btn(self)->ElementHandle:
        return self.page.locator('(//*[@class="search-components-btn"])')

    def search_component(self):
        self.bubblely_menu.click()
        self.official_homepage_menu.click()
        self.page_component.click()
        self.select_country.click()
        self.select_country_details.click()
        self.search_components_btn.click()

