from pagesPOM.base_page import Base
from playwright.sync_api import ElementHandle
from playwright.sync_api import expect
class LoginPage(Base):

    @property
    def login1_btn(self)->ElementHandle:
        return self.page.locator('(//*[@class="login"])[3]')

    @property
    def username_input(self) -> ElementHandle:
        return self.page.locator("//input[@id='user_id']")

    @property
    def password_input(self) -> ElementHandle:
        return self.page.locator("//input[@id='user_pwd']")

    @property
    def login2_btn(self) -> ElementHandle:
        return self.page.locator("//*[@id='btn-login']")

    @property
    def alert_sms(self) -> ElementHandle:
        return self.page.locator("//*[text()='Check your ID or password.']")

    @property
    def logo_partner(self) -> ElementHandle:
        return self.page.locator("//*[@id='logo']")

    def goto_base_url(self):
        self.page.goto(self.url)

    def login(self, username, password):
        self.goto_base_url()
        self.login1_btn.click()
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login2_btn.click()
    print("xuan test")
    def verify_login_failed(self):
        expect(self.alert_sms).to_be_visible()

