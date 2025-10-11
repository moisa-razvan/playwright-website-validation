import time
import asyncio
from playwright.async_api import async_playwright
from pages import checkout, cart, shop


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://valentinos-magic-beans.click/")

        await shop.go_to_shop_page(page)
        (first_product_name,first_product_price) = await shop.add_product_to_cart(page, 2)

        await cart.check_product_name(page, first_product_name)
        await cart.go_to_cart(page)

        await cart.click_proceed_to_checkout(page)
        await checkout.fill_contact_info(page)
        await checkout.fill_payment_info(page)
        await checkout.fill_shipping_address(page)

        time.sleep(2)
        await browser.close()

asyncio.run(main())