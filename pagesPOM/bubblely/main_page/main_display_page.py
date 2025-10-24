from playwright.sync_api import Page, ElementHandle
from Util.common_locator import CommonLocator
from config_pack.environment import EnvConfig
import os

from tests.conftest import load_env


class main_display_page(Page):

    def   __init__(self, page: Page):
        self.page = page
        self.env = EnvConfig()
    def open_mainpage(self,load_env):
        self.page.goto(f"{self.env.MAIN_PAGE_URL}/en/showcase")


