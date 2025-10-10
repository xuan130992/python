from playwright.sync_api import sync_playwright
from pagesPOM.login_page import LoginPage
import os
def test_save_login_state():
    os.makedirs("./auth", exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False,slow_mo=500)
        context = browser.new_context()
        page = context.new_page()

        login_page = LoginPage(page)
        login_page.login(username='lexuan.vn@smilegate.com', password='Hoilamgi123!')

        context.storage_state(path="./auth/storage_state.json")
        browser.close()
