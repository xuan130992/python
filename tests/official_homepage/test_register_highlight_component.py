from playwright.sync_api import Page,ElementHandle
from pagesPOM.bubblely.Official_homepage.register_component import register_component
from pagesPOM.bubblely.Official_homepage.register_feature_component_page import register_feature_component
from Util.common_locator import CommonLocator
from Util.common_functions import CommonFunctions
from pagesPOM.bubblely.main_page.main_display_page import main_display_page
from config_pack.environment import EnvConfig
import os


def test_register_highlight_component(load_env,page:Page):
    os.makedirs("auth", exist_ok=True)
    page.context.storage_state(path="auth/storage_state.json")
    register_component1=register_component(page)
    register_feature_component1=register_feature_component(page)
    common_locator1=CommonLocator(page)
    common_function1=CommonFunctions(page)
    main_display_page1=main_display_page(page)
    env=EnvConfig()
    page.goto(f"{env.BASE_URL}/main")
    register_component1.register_component_act("Korea","Highlight Mod")
    register_feature_component1.register_feature_component(common_locator1.feature_title,"0",common_locator1.EN_highlight_title)
    common_function1.verify_register_successful(common_locator1)
    main_display_page1.open_mainpage(load_env)
    common_function1.verify_mod_displayed(common_locator1.EN_highlight_title,common_locator1)