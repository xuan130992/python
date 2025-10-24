import playwright
from playwright.sync_api import sync_playwright, Page

from pagesPOM.base_page import Base
import pytest
from pagesPOM.login_page import LoginPage
from pagesPOM.bubblely.Official_homepage.register_component import register_component
from pagesPOM.bubblely.Official_homepage.register_banner import registerbanner_page
from Util.common_functions import CommonFunctions
from Util.common_locator import CommonLocator
from pagesPOM.bubblely.main_page.main_display_page import main_display_page
from config_pack.environment import EnvConfig
import os
from dotenv import load_dotenv

def test_register_banner_successful(load_env,page:Page):
    os.makedirs("auth", exist_ok=True)
    page.context.storage_state(path="auth/storage_state.json")
    login_page1 = LoginPage(page)
    register_component1=register_component(page)
    register_banner_page1 = registerbanner_page(page)
    common_locator = CommonLocator(page)
    common_functions = CommonFunctions(page)
    main_display_page1 = main_display_page(page)
    env=EnvConfig()
    login_page1.login(username='lexuan.vn@smilegate.com', password='Hoilamgi123!')
    page.goto(f"{env.BASE_URL}/main")
    print("Current URL:", page.url)
    register_component1.register_component_act("korea","Banner")
    register_banner_page1.register_banner_component(common_locator.feature_title,"0","https://accounts.gate8.com/")
    common_functions.upload_image("xpath=(//*[contains(text(),'Upload')])[1]","./resourse/banner_images/png_1300x325.png")
    common_functions.upload_image("xpath=(//*[contains(text(),'Upload')])[2]","./resourse/banner_images/png_1138x210.png")
    register_banner_page1.register_btn_act()
    common_functions.verify_register_successful(common_locator)
    main_display_page1.open_mainpage(load_env)
    common_functions.verify_banner_display(common_locator)


