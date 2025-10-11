async def fill_order_and_email(page, order_id, email):
    await page.locator("[data-test-id='contact-order-id-input']").fill(order_id)
    await page.locator("[data-test-id='contact-email-input']").fill(email)

async def click_track_order(page,button_name):
    await page.get_by_role("button", name=button_name).click()