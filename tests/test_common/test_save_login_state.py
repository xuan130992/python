from playwright.sync_api import sync_playwright
from pagesPOM.login_page import LoginPage
import os
def test_save_login_state():
    try:
        os.makedirs("auth", exist_ok=True)
        print("Folder 'auth' created or already exists.")
    except Exception as e:
        print(" Failed to create 'auth' folder:", e)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False,slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        print("bat dau run")
        login_page = LoginPage(page)
        login_page.login(username='lexuan.vn@smilegate.com', password='Hoilamgi123!')

        page.wait_for_url("https://partners-qa.onstove.com/main")
        print("Saving storage state...")

        context.storage_state(path="auth/storage_state.json")
        print("Saved successfully.")


        browser.close()

