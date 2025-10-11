import time
import asyncio
from playwright.async_api import async_playwright, expect
from pages import checkout, cart, shop, contact


async def main():
    async with async_playwright() as p:

        # open browser and go to page
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://valentinos-magic-beans.click/")

        # go to shop page & add 1 product into cart
        await shop.go_to_shop_page(page)
        (first_product_name,first_product_price) = await shop.add_product_to_cart(page, 2)

        # go to cart page and check name and price
        await cart.go_to_cart(page)
        assert await cart.check_product_name(page, first_product_name)
        assert await cart.compare_cart_price_with_summary_price(page, first_product_price)

        # go to checkout page & fill content & click place order
        await cart.click_proceed_to_checkout(page)
        await checkout.fill_contact_info(page)
        await checkout.fill_payment_info(page)
        await checkout.fill_shipping_address(page)
        await checkout.click_place_order(page)

        # store the order id
        order_id = await page.get_by_text("Your Order ID is").locator("..").get_by_role("paragraph").nth(1).text_content()

        # click track your order & fill email and order id & click track order
        await contact.click_track_order(page, "Track Your Order")
        await contact.fill_order_and_email(page, order_id, checkout.values["email"])
        await contact.click_track_order(page, "Track Order")
        time.sleep(0.5)

        # compare the name and price from order page, with stored name and price
        assert await page.locator(".space-y-4").get_by_role("paragraph").nth(0).text_content() == first_product_name
        assert await page.get_by_text("$").text_content() == first_product_price

        await browser.close()

asyncio.run(main())