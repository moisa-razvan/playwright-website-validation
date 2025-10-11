import json
import time
import asyncio
from playwright.async_api import async_playwright

from valentinos_magic_beans.python.pages import shop


# async def main():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=False)
#         page = await browser.new_page()
#

#        # display the requests from page
#         page.on("request", lambda request: print(request.url, request.method))
#         await page.goto("https://valentinos-magic-beans.click/")
#         await page.wait_for_load_state("networkidle")
#
#         await browser.close()
#
# asyncio.run(main())

# async def main():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=False)
#         page = await browser.new_page()
#
#         # replace products with specified data
#
#         await page.route(
#             "https://api.valentinos-magic-beans.click/products",
#             lambda route: route.fulfill(
#                 status=200,
#                 content_type="application/json",
#                 body=json.dumps({
#                     "success": True,
#                     "source": "dynamodb",
#                     "data": [
#                         {
#                             "name": "Good stuff",
#                             "price": 55,
#                             "id": 0
#                         },
#                         {
#                             "name": "Simple coffee",
#                             "price": 5,
#                             "id": 1
#                         }
#                     ]
#                 })
#             )
#         )
#
#         await page.goto("https://valentinos-magic-beans.click/products")
#         await page.wait_for_load_state("networkidle")
#         time.sleep(10)
#
#         await browser.close()
#
# asyncio.run(main())


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        # block images from showing up on page

        async def handle_route(route):
            if route.request.resource_type == "image":
                await route.abort()
            else:
                await route.continue_()

        await page.route("**/*", handle_route)

        await page.goto("https://valentinos-magic-beans.click/products")
        await page.wait_for_load_state("networkidle")

        await browser.close()


asyncio.run(main())
