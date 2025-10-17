from playwright.sync_api import Page,ElementHandle,Locator
import uuid
class CommonLocator(Page):
    def __init__(self, page: Page):
        self.page = page
        self.iframe = page.frame_locator("#iframe-BLZ00000001004")
        self.random_suffix = uuid.uuid4().hex[:6]
        self.feature_title = f"feature mod component_{self.random_suffix}"
        self.EN_feature_title= "en_feature_component"
        self.EN_normal_title = "en_normal_component"
        self.EN_highlight_title = "en_highlight_component"
        self.EN_ranking_title = "en_ranking_component"


    @property
    def registed_components(self) -> Locator:
        return self.iframe.locator(f'(//*[@title="{self.feature_title}"])[1]')

    @property
    def component_title(self)-> Locator:
        return self.page.locator(f'xpath=(//*[contains(text(),"{self.feature_title}")])[1]')

    @property
    def feature_title_en(self)-> Locator:
        return self.page.locator(f'xpath=(//*[contains(text(),"{self.EN_feature_title}")])[1]')
    @property
    def normal_title_en(self)-> Locator:
        return self.page.locator(f'xpath=(//*[contains(text(),"{self.EN_normal_title}")])[1]')
    @property
    def highlight_title_en(self)-> Locator:
        return self.page.locator(f'xpath=(//*[contains(text(),"{self.EN_highlight_title}")])[1]')
    @property
    def ranking_title_en(self)-> Locator:
        return self.page.locator(f'xpath=(//*[contains(text(),"{self.EN_ranking_title}")])[1]')

