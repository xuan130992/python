from playwright.sync_api import Page,ElementHandle,Locator
import uuid
class CommonLocator(Page):
    def __init__(self, page: Page):
        self.page = page
        self.iframe = page.frame_locator("#iframe-BLZ00000001004")
        self.random_suffix = uuid.uuid4().hex[:6]
        self.feature_title = f"feature mod component_{self.random_suffix}"

    @property
    def registed_components(self) -> Locator:
        return self.iframe.locator(f'(//*[@title="{self.feature_title}"])[1]')

    @property
    def component_title(self)-> Locator:
        return self.page.locator(f'xpath=(//*[contains(text(),"{self.feature_title}")])[1]')
