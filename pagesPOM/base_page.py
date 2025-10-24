from playwright.sync_api import  Page

import config_pack.environment
from config_pack.environment import EnvConfig
class Base(object):
    def __init__(self, page:Page):
        self.page = page
        self.url=(f"{EnvConfig().BASE_URL}/")
        print("run on ENV ",EnvConfig.ENV)
