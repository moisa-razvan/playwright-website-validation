import asyncio
from playwright.async_api import async_playwright


async def go_to_shop_page(page):
    await page.get_by_role("button", name="Shop Coffee").click(timeout=2000)

async def add_product_to_cart(page, index):
    assert await page.get_by_role("heading", name="Our Coffee Collection").is_visible()

    product_list = page.locator(".p-6")
    product_name = await product_list.nth(index).get_by_role("heading").text_content()
    product_price = await product_list.nth(index).locator(".font-bold").text_content()
    add_to_cart = product_list.nth(index).get_by_role("button", name="Add to Cart")

    await add_to_cart.click()
    return product_name,product_price