from pytest_bdd import scenarios, parsers, parsers, given, when, then
import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage

scenarios()
@pytest.fixture(scope="module")
def login_page(page:Page):
    return LoginPage(page)
@given("I go to partner login page")
def i_go_to_partner_login_page(login_page):
   login_page.goto_baseurl()

@when("I input valid credential on the partner login page")
def i_input_valid_credential(login_page):
    login_page.login()


