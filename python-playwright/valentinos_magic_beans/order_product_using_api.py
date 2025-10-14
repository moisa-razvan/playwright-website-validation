import requests
import asyncio
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://valentinos-magic-beans.click/")

        response = requests.get("https://api.valentinos-magic-beans.click/products")
        response_body = response.json()

        # check status code
        assert response.status_code == 200

        # check that the data from body is not empty
        assert len(response_body["data"]) > 0

        products = response_body["data"]
        available_product = []
        for item in products:
            if item["stock"] > 0:
                available_product.append(item)
                break

        body_api = {
            "customerDetails": {
                "firstName": "Timon",
                "lastName": "Dragoneer",
                "email": "myemail1825date@gmail.com",
                "address": "Good street",
                "city": "Good ciry",
                "zipCode": "12345",
                "country": "Good state",
            },
            "items": [{"productId": available_product[0]["id"], "quantity": 1}],
        }

        order_response = requests.post("https://api.valentinos-magic-beans.click/orders", json=body_api)

        assert order_response.status_code == 201

        await browser.close()


asyncio.run(main())
