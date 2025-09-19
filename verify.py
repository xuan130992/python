
import pytest
from playwright.async_api import async_playwright
from LoginPagewithWait import run


async def test_login(page):
    async with async_playwright() as playwright:
        page, browser = await run(playwright)
        current_url =page.url
        expect_url = "https://partners-qa.onstove.com/main"
        assert current_url == expect_url
