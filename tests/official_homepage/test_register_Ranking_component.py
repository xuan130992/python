from playwright.sync_api import Playwright,Page
from pagesPOM.bubblely.Official_homepage.register_Mod_component_page import register_Mod_component
from Util.common_locator import CommonLocator
from Util.common_functions import CommonFunctions
from config_pack.environment import EnvConfig
import os

from pagesPOM.bubblely.Official_homepage.register_component import register_component


def test_register_ranking_component(load_env,page:Page):
    os.makedirs("auth", exist_ok=True)
    page.context.storage_state(path="auth/storage_state.json")
    register_component1=register_component(page)
    register_Mod_component1=register_Mod_component(page)
    CommonLocator1=CommonLocator(page)
    CommonFunctions1=CommonFunctions(page)
    env=EnvConfig()
    page.goto(f'{env.BASE_URL}/main')
    register_component1.register_component_act("Korea","Ranking")
    register_Mod_component1.register_ranking_component(CommonLocator1.Ranking_title,"0",CommonLocator1.EN_ranking_title)
    CommonFunctions1.verify_register_successful(CommonLocator1,"Ranking")
