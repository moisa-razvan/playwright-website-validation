import time
import asyncio
from playwright.async_api import async_playwright
from pages import shop, cart


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://valentinos-magic-beans.click/")

        await shop.go_to_shop_page(page)
        (first_product_name,first_product_price) = await shop.add_product_to_cart(page, 1)

        await cart.go_to_cart(page)

        assert await cart.check_product_name(page, first_product_name)

        # print(await page.get_by_text("Subtotal").locator("..").locator(".font-semibold").text_content())
        assert await cart.compare_cart_price_with_summary_price(page, first_product_price)
        time.sleep(1)
        await browser.close()

asyncio.run(main())