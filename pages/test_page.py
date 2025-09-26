import pytest
from playwright.async_api import Page,expect
from pages import login_page
from pages.login_page import LoginPage
from pages.partner_page import partner_page


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return{
        **browser_type_launch_args,
        "headless": False,
        "slow_mo": 500,
    }




def test_login_tc_01(page: Page):
    login_page=LoginPage(page)
    login_page.login("lexuan.vn@smilegate.com","Hoilamgi123!")
    partner_page1 = partner_page(page)
    partner_page1.verify_logo(page)
    



def test_login_tc_02(page: Page):
    login_page=LoginPage(page)
    login_page.login("lexuan.vn","Hoilamgi1231")
    login_page.verify_login_failed_alert()




