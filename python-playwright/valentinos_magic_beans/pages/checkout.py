from valentinos_magic_beans.utils import values

values = values.values

async def fill_contact_info(page):
    await page.locator("[data-test-id=\"checkout-firstname-input\"]").fill(values["first_name"])
    await page.locator("[data-test-id=\"checkout-lastname-input\"]").fill(values["last_name"])
    await page.locator("[data-test-id=\"checkout-email-input\"]").fill(values["email"])

async def fill_shipping_address(page):
    await page.locator("[data-test-id=\"checkout-address-input\"]").fill(values["address"])
    await page.locator("[data-test-id=\"checkout-city-input\"]").fill(values["city"])
    await page.locator("[data-test-id=\"checkout-zipcode-input\"]").fill(values["zip"])
    await page.locator("[data-test-id=\"checkout-country-input\"]").fill(values["state"])

async def fill_payment_info(page):
    await page.locator("[data-test-id=\"checkout-cardname-input\"]").fill(values["payment"]["name"])
    await page.locator("[data-test-id=\"checkout-cardnumber-input\"]").fill(values["payment"]["card_number"])
    await page.locator("[data-test-id=\"checkout-cardexpiry-input\"]").fill(values["payment"]["expiration_date"])
    await page.locator("[data-test-id=\"checkout-cardcvc-input\"]").fill(values["payment"]["CVC"])

async def click_place_order(page):
    await page.locator("[data-test-id='place-order-button']").click()

