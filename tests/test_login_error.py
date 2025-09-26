from playwright.sync_api import Page
from pagesPOM.login_page import LoginPage


def test_login_error(page:Page):
    login_page = LoginPage(page)
    login_page.login(username='lexuan.vn@smilegate.com', password='Hoilamgi123')
    login_page.verify_login_failed()