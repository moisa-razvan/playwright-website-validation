
async def go_to_cart(page):
    await page.locator("[data-test-id=\"header-cart-button\"]").get_by_role("button").click()

async def check_product_name(page, product_name):
    return await page.get_by_role("heading", name=product_name).is_visible()

async def compare_cart_price_with_summary_price(page, price):
    return await page.get_by_text("Subtotal").locator("..").get_by_text("$").text_content() == price
    # return await page.get_by_text("Subtotal").locator("..").locator(".font-semibold").text_content() == price

async def click_proceed_to_checkout(page):
    await page.locator("[data-test-id=\"proceed-to-checkout\"]").click()