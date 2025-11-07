from playwright.sync_api import Page,expect, ElementHandle


from Util import common_locator
from pagesPOM.base_page import Base
from Util.common_locator import CommonLocator
import uuid
class CommonFunctions(Base):


    def __init__(self,page: Page):
        self.page = page
        self.iframe = page.frame_locator("#iframe-BLZ00000001004")


    def upload_image(self, upload_locator:str, filepath:str):
        print("Upload thành công.")
        with self.page.expect_file_chooser() as fc_info:
             self.iframe.locator(upload_locator).click()
             file_chooser=  fc_info.value
             file_chooser.set_files(filepath)

    def verify_register_successful(self,common_locator: CommonLocator,component_type: str):
        expect(common_locator.registed_components(component_type)).to_be_visible()

    def verify_banner_display(self,common_locator: CommonLocator,component_type: str):
        expect(common_locator.component_title(component_type)).to_be_visible()

    def verify_mod_displayed(self,common_type: str,common_locator: CommonLocator):
        if common_type == "Featured Mod":
            expect(common_locator.feature_title_en).to_be_visible()
        elif common_type == "Normal":
            expect(common_locator.normal_title_en).to_be_visible()
        elif common_type == "Ranking":
            expect(common_locator.ranking_title_en).to_be_visible()
        elif common_type == "Highlight":
            expect(common_locator.highlight_title_en).to_be_visible()




