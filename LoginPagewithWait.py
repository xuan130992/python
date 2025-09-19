import asyncio

from playwright.async_api import async_playwright, Playwright


async def run(playwright: Playwright):
    browser = await playwright.chromium.launch(headless=False,slow_mo=500)
    page = await browser.new_page()
    await page.goto("https://partners-qa.onstove.com/")
    log_in_button = page.get_by_role("link",name="Log in").first
    await log_in_button.click()

    user_name = page.get_by_placeholder("ID or Email")
    await user_name.highlight()
    await user_name.fill("lexuan.vn@smilegate.com")

    password = page.get_by_placeholder("Password")
    await password.highlight()
    await password.fill("Hoilamgi123!")

    login_button = page.get_by_role("button",name="Log In")
    await login_button.click()

    return page ,browser










    await page.close()


async def main():
    async with async_playwright()as playwright:
        await run(playwright)
asyncio.run(main())