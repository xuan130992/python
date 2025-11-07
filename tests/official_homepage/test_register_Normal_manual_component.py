
from playwright.sync_api import Playwright, Page

from Util import common_locator
from pagesPOM.bubblely.Official_homepage.register_component import register_component
from pagesPOM.bubblely.Official_homepage.register_normal_component_page import register_normal_component
from pagesPOM.bubblely.main_page.main_display_page import main_display_page
from Util.common_locator import CommonLocator
from Util.common_functions import CommonFunctions
import os
from config_pack.environment import EnvConfig

def test_register_Normal_manual_component_successful(load_env,page:Page):
    os.makedirs("auth",exist_ok=True)
    page.context.storage_state(path="auth/storage_state.json")
    #login_page = LoginPage(page)
    register_component1 = register_component(page)
    register_normal_component1 = register_normal_component(page)
    common_locator1 = CommonLocator(page)
    common_functions1 = CommonFunctions(page)
    main_display_page1 = main_display_page(page)
    env = EnvConfig()
    page.goto(f"{env.BASE_URL}/main")
    register_component1.register_component_act("korea","Normal Mod")
    register_normal_component1.register_normal_manual_component(common_locator1.Normal_mod_title,"0",common_locator1.EN_normal_title)
    common_functions1.verify_register_successful(common_locator1,"Normal Mod")
    main_display_page1.open_mainpage(load_env)
    common_functions1.verify_mod_displayed(common_locator1.EN_normal_title,common_locator1)
def test_register_auto_component_successful(load_env,page:Page):
    os.makedirs("auth",exist_ok=True)
    page.context.storage_state(path="auth/storage_state.json")
    register_component1 = register_component(page)
    register_normal_component1 = register_normal_component(page)
    common_locator1 = CommonLocator(page)
    common_functions1 = CommonFunctions(page)
    main_display_page1 = main_display_page(page)
    env = EnvConfig()
    page.goto(f"{env.BASE_URL}/main")
    register_component1.register_component_act("korea","Normal Mod")
    register_normal_component1.register_normal_auto_component(common_locator1.Normal_mod_title,"0",common_locator1.EN_normal_title)
    common_functions1.verify_register_successful(common_locator1,"Normal Mod")
    main_display_page1.open_mainpage(load_env)
    common_functions1.verify_mod_displayed(common_locator1.EN_normal_title,common_locator1)






