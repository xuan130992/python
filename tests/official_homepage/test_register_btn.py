from playwright.sync_api import Page
from pagesPOM.bubblely.Official_homepage.register_component import  register_component
from pagesPOM.login_page import LoginPage
import pytest

@pytest.mark.skip(reason="Tạm thời bỏ qua test này")
def test_register_successful(page:Page):
    login_page = LoginPage(page)
    register_component1 = register_component(page)
    login_page.login(username='lexuan.vn@smilegate.com', password='Hoilamgi123!')
    register_component1.register_component_act("korea")
    register_component1.verify_register_btn()
