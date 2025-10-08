from playwright.sync_api import Page,expect
from pagesPOM.base_page import Base
import uuid
class CommonFunctions(Base):
    def __init__(self,page: Page):
        self.page = page
        self.random_suffix = uuid.uuid4().hex[:6]
        self.feature_title = f"feature mod component_{self.random_suffix}"
    def upload_image(self, upload_locator:str, filepath:str):
        with self.page.expect_file_chooser() as fc_info:
             self.page.locator(upload_locator).click()
        file_chooser=  fc_info.value
        file_chooser.set_files(filepath)