import time
import re
from playwright.sync_api import sync_playwright, expect
import asyncio
from playwright.async_api import async_playwright

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto(" ")
#     browser.close()


# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto("https://www.emag.ro/")
#     page.fill("input#searchboxTrigger", "9070 XT")
#     page.click("button[class='btn btn-default searchbox-submit-button']")
#     page.get_by_label("preț minim").fill("2000")
#     page.get_by_label("preț maxim").fill("4000")
#     time.sleep(0.25)
#     page.get_by_label("Aplică filtrul de preț personalizat").click()
#     time.sleep(5)
#     browser.close()

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto("https://store.steampowered.com/")
#     # expect(page).to_have_title("")
#     search_bar = page.get_by_placeholder("Search the store")
#     assert search_bar.is_visible()
#     search_bar.fill("Path of exile")
#     page.locator("button[type='submit']").click()
#
#     link_list = page.get_by_role("link")
#     first_link = link_list.nth(10)
#     print(first_link.text_content())
#
#     page.get_by_role("link", name="Path of Exile 23 Oct, 2013").click()
#     browser.close()

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto("http://localhost:5000/")
#     assert page.get_by_role("button", name="Accept").is_visible()
#     assert page.get_by_role("button", name="Decline").is_visible()
#
#     page.get_by_role("button", name="Accept").click()
#     assert not page.get_by_role("button", name="Accept").is_visible()
#     assert not page.get_by_role("button", name="Decline").is_visible()
#
#     page.get_by_text("Go to Feedback Form").click()
#
#     # page_title = page.get_by_text("Feedback Form").first
#     page_title = page.get_by_role("heading", name="Feedback Form")
#     assert page_title.is_visible()
#
#     # hidden_button_text = page.get_by_text("Hidden feature")
#     # assert hidden_button_text.is_visible()
#
#     # hidden_button_role = page.get_by_role("button", name="Hidden feature")
#     # hidden_button_role_text = hidden_button_role.text_content()
#     # assert hidden_button_role.is_visible()
#
#     #hidden_button_text will display even hidden text, meanwhile hidden_button_role_text will not see the hidden text
#
#     time.sleep(1)
#     browser.close()


# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto("http://localhost:5000/FeedBackForm.html")
#
#     invalid_text = page.get_by_text("Invalid email format")
#     assert not invalid_text.is_visible()
#
#     page.get_by_role("textbox", name="email").fill("asd")
#     assert invalid_text.is_visible()
#     time.sleep(1)
#     browser.close()

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto("https://www.youtube.com/results?search_query=sabaton+bismarck")
#     page.get_by_role("button", name="Accept the use of cookies").click()
#     time.sleep(3)
#     page.get_by_role("link", name="SABATON - Bismarck (Official Music Video) 6 minutes, 10 seconds").click()
#     time.sleep(2)
#     browser.close()
#



# async def main():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=False)
#         page = await browser.new_page()
#         await page.goto("https://www.youtube.com/results?search_query=sabaton+bismarck")
#         await page.get_by_role("button", name="Accept the use of cookies").click()
#         await page.get_by_role("link", name="SABATON - Bismarck (Official Music Video) 6 minutes, 10 seconds").click()
#         await browser.close()
#
# asyncio.run(main())

# async def main():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=False)
#         page = await browser.new_page()
#         await page.goto("https://www.youtube.com")
#         await page.get_by_role("button", name="Accept the use of cookies").click()
#         await page.get_by_role("button", name="Search with your voice").click()
#         time.sleep(5)
#         await browser.close()
#
# asyncio.run(main())

# import asyncio
# import time
# from playwright.async_api import async_playwright
#
# async def main():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=False)
#         context = await browser.new_context()
#
#         # ✅ Make sure all values are strings (except expires which is int)
#         cookie1 = {
#             'name': 'gdpr_consent_type',
#             'value': '1',
#             'url': 'https://www.emag.ro/',
#         }
#         cookie2 = {
#             'name': 'gdpr_consent_version',
#             'value': '5',
#             'url': 'https://www.emag.ro/',
#         }
#
#         # ✅ This will now be accepted by context.add_cookies()
#         await context.add_cookies([cookie1,cookie2])
#
#         page = await context.new_page()
#         await page.goto('https://www.emag.ro/')
#
#         # Print cookies to verify
#         cookies = await context.cookies()
#         print(cookies)
#
#         time.sleep(3)
#         await browser.close()
#
# asyncio.run(main())

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
            viewport={'width': 2000, 'height': 720},
        )
        page = await context.new_page()
        await page.goto("https://www.youtube.com")
        time.sleep(3)
        await browser.close()

asyncio.run(main())