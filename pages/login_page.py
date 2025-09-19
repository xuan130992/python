from playwright.sync_api import Page,expect


class LoginPage:
    def __init__(self, page:Page):
        self.page = page
        self.page.goto("https://partners-qa.onstove.com/")
        self.login1_btn=self.page.locator('(//*[@class="login"])[3]')
        print("step 0: login roi")
        self.username_input=self.page.locator('//input[@id="user_id"]')
        self.password_input=self.page.locator("//input[@id='user_pwd']")
        self.login2_btn= self.page.locator("//*[@id='btn-login']")
        self.alert_sms= self.page.locator("//*[text()='Check your ID or password.']")

    def login(self, username, password):
        self.login1_btn.click()
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login2_btn.click()

    def verify_login_failed_alert(self ):
        expect(self.alert_sms).to_have_text("Check your ID or password.")