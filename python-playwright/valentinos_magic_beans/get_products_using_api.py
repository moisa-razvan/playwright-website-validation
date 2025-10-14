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

        # check header's content type
        assert response.headers["Content-Type"] == "application/json"

        # check that the data from body is not empty
        assert len(response_body["data"]) > 0

        coffee_name = []
        for item in response_body["data"]:
            coffee_name.append(item["name"])

        await browser.close()


asyncio.run(main())
