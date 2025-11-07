from playwright.sync_api import Page,ElementHandle,Locator
import uuid
class CommonLocator(Page):
    def __init__(self, page: Page):
        self.page = page
        self.iframe = page.frame_locator("#iframe-BLZ00000001004")
        self.random_suffix = uuid.uuid4().hex[:6]
        #component title list
        self.feature_title = f"feature mod component_{self.random_suffix}"
        self.Hero_banner_title = f"Hero Banner {self.random_suffix}"
        self.Banner_title = f"Banner {self.random_suffix}"
        self.Normal_mod_title = f"Normal Mod {self.random_suffix}"
        self.Highlight_title = f"EN highlight {self.random_suffix}"
        self.Ranking_title = f"Ranking {self.random_suffix}"
        # component title display
        self.EN_feature_title= "en_feature_component"
        self.EN_normal_title = "en_normal_component"
        self.EN_highlight_title = "en_highlight_component"
        self.EN_ranking_title = "en_ranking_component"



    def registed_components(self,component_type:str) -> Locator:
        if component_type=="feature":
            return self.iframe.locator(f'(//*[@title="{self.feature_title}"])[1]')
        elif component_type=="Hero Banner":
            return self.iframe.locator(f'(//*[@title="{self.Hero_banner_title}"])[1]')
        elif component_type=="Banner":
            return self.iframe.locator(f'(//*[@title="{self.Banner_title}"])[1]')
        elif component_type=="Normal Mod":
            return self.iframe.locator(f'(//*[@title="{self.Normal_mod_title}"])[1]')
        elif component_type=="Highlight Mod":
            return self.iframe.locator(f'(//*[@title="{self.Highlight_title}"])[1]')
        elif component_type=="Ranking":
            return self.iframe.locator(f'(//*[@title="{self.Ranking_title}"])[1]')
        else:
            raise ValueError("no any component")


    def component_title(self,component_type:str)-> Locator:
        if component_type=="feature":
            return self.page.locator(f'xpath=(//*[contains(text(),"{self.feature_title}")])[1]')
        if component_type=="Hero Banner":
            return self.page.locator(f'xpath=(//*[contains(text(),"{self.Hero_banner_title}")])[1]')
        if component_type=="Banner":
            return self.page.locator(f'xpath=(//*[contains(text(),"{self.Banner_title}")])[1]')
        if component_type=="Standard":
            return self.page.locator(f'(//*[contains(text(),"{self.Normal_mod_title}")])[1]')
        if component_type=="Highlight":
            return self.page.locator(f'xpath=(//*[contains(text(),"{self.Highlight_title}")])[1]')
        if component_type=="Ranking":
            return self.page.locator(f'xpath=(//*[contains(text(),"{self.Ranking_title}")])[1]')
        else:
            raise ValueError("no any component to input")

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

