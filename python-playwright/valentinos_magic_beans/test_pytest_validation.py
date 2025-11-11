import time
import random

from playwright.sync_api import Playwright


def test_add_item_to_cart_by_name(playwright: Playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://valentinos-magic-beans.click")
    page.get_by_role("button", name="Shop Coffee").click()

    brazilian_coffee = page.locator(".p-0").filter(has_text="Brazilian Santos")
    guatemalan_coffee = page.locator(".p-0").filter(has_text="Guatemalan Volcano")
    brazilian_coffee.get_by_role("button", name="Add to Cart").click()
    guatemalan_coffee.get_by_role("button", name="Add to Cart").click()

    # number_of_products = random.randint(1, 6)
    # for product in range(number_of_products):
    #     page.locator(".p-0").nth(random.randint(0, 5)).get_by_role("button", name="Add to Cart").click()

    page.locator('[data-test-id="header-cart-button"]').get_by_role("button").click()
    time.sleep(3)


def test_table(playwright: Playwright):
    browser = playwright.firefox.launch()
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://www.rahulshettyacademy.com/seleniumPractise/#/offers")

    products_list = []
    table_row = page.locator("tr")
    for i in range(1, table_row.count()):
        product_and_price = dict(
            product=table_row.nth(i).locator("td").nth(0).text_content(),
            price=table_row.nth(i).locator("td").nth(1).text_content(),
        )

        products_list.append(product_and_price)

    print(products_list)
