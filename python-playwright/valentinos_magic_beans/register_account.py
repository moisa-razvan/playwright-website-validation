import time
import asyncio
from playwright.async_api import async_playwright
from pages import sign_up
from valentinos_magic_beans.utils import emailUtils


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://valentinos-magic-beans.click/")
        email_utils = emailUtils.emailUtils()

        inbox = email_utils.createInbox()

        await sign_up.go_to_sign_up(page)

        await sign_up.fill_sign_up_form(page, inbox)

        await sign_up.click_create_account(page)

        email = await email_utils.waitForMail(inbox.id)
        print(email)

        time.sleep(2)
        await browser.close()

asyncio.run(main())