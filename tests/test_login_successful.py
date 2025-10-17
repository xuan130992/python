from playwright.sync_api import Page
from pagesPOM.login_page import LoginPage
from pagesPOM.partner_page import partner_page
from playwright.sync_api import sync_playwright

def test_login_success(page: Page):
    login_page = LoginPage(page)

    partner_page1= partner_page(page)
    login_page.login(username='lexuan.vn@smilegate.com', password='Hoilamgi123!')
    partner_page1.verify_login_success()
    print('Login Success')