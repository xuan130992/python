import random
import string
import uuid

from playwright.sync_api import Page

from Util.common_functions import  CommonFunctions
from Util.common_locator import CommonLocator

from pagesPOM.bubblely.Official_homepage.register_component import register_component
from pagesPOM.login_page import LoginPage
from pagesPOM.bubblely.Official_homepage.register_feature_component_page import register_feature_component
from pagesPOM.bubblely.main_page.main_display_page import main_display_page

def test_register_feature_component_successful(page:Page):
    page.context.storage_state(path="auth/storage_state.json")
    login_page = LoginPage(page)
    register_component1 = register_component(page)
    register_feature_component1 = register_feature_component(page)
    common_locator = CommonLocator(page)
    common_functions = CommonFunctions(page)
    main_display_page1 = main_display_page(page)
    page.goto("https://partners-qa.onstove.com/main")
    #login_page.login(username='lexuan.vn@smilegate.com', password='Hoilamgi123!')
    register_component1.register_component_act("korea","Featured Mod")
    register_feature_component1.register_feature_component(common_locator.feature_title,"0",common_locator.EN_feature_title)
    common_functions.verify_register_successful(common_locator)
    main_display_page1.open_mainpage()
    page.wait_for_timeout(5000)
    common_functions.verify_mod_displayed(common_locator.EN_feature_title,common_locator)
    page.wait_for_timeout(2000)
