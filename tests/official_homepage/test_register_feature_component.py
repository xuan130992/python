import random
import string

from playwright.sync_api import Page

from pagesPOM.bubblely.Official_homepage.register_component import register_component
from pagesPOM.login_page import LoginPage
from pagesPOM.bubblely.Official_homepage.register_feature_component_page import register_feature_component

def test_register_feature_component_successful(page,):

    login_page = LoginPage(page)
    register_component1 = register_component(page)
    register_feature_component1 = register_feature_component(page)
    login_page.login(username='lexuan.vn@smilegate.com', password='Hoilamgi123!')
    register_component1.register_component_act("korea")
    register_feature_component1.register_feature_component(register_feature_component1.feature_title,"0","en_featuremod_component")
    register_feature_component1.verify_register_successful()