from playwright.sync_api import sync_playwright
from config_pack.environment import EnvConfig
import config_pack.environment
from pagesPOM.login_page import LoginPage
from dotenv import load_dotenv
import os

def test_save_login_state(load_env):
    os.makedirs("auth", exist_ok=True)
    env= EnvConfig()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False,slow_mo=500)
        context = browser.new_context()
        page = context.new_page()

        print("bat dau run")
        login_page = LoginPage(page)
        login_page.login(username=env.USERNAME, password=env.PASSWORD)
        print(f"user name la {env.USERNAME}")
        print(f"password la {env.PASSWORD}")

        page.wait_for_url(f"{env.BASE_URL}/main")
        print("Saving storage state...")

        context.storage_state(path="auth/storage_state.json")
        print("Saved successfully.")


        browser.close()

