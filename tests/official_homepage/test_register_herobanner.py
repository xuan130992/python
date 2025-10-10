from playwright.async_api import Page

from Util.common_locator import CommonLocator
from pages.login_page import LoginPage
from pagesPOM.bubblely.Official_homepage.register_banner import registerbanner_page
from pagesPOM.bubblely.Official_homepage.register_component import register_component
from Util.common_functions import CommonFunctions

def test_register_banner_successful(page):
    login_page1 = LoginPage(page)

    register_component1=register_component(page)
    register_banner_page1 = registerbanner_page(page)
    common_locator = CommonLocator(page)
    common_functions = CommonFunctions(page)
    #login_page1.login(username='lexuan.vn@smilegate.com', password='Hoilamgi123!')
    register_component1.register_component_act("korea","Hero Banner")
    register_banner_page1.register_hero_banner_component(common_locator.feature_title,"0","0","https://jira.smilegate.net/browse/BBZG-3725")
    common_functions.upload_image("xpath=(//*[contains(text(),'Upload')])[1]","./resourse/banner_images/png_2560x542.png")
    common_functions.upload_image("xpath=(//*[contains(text(),'Upload')])[2]","./resourse/banner_images/png_1364x642.png")
    register_banner_page1.register_btn_act()
    common_functions.verify_register_successful(common_locator)
