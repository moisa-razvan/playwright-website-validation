from valentinos_magic_beans.utils import emailUtils, values

async def go_to_sign_up(page):
    await page.get_by_role("button", name="Sign Up").click()

async def fill_sign_up_form(page, inbox):
    await page.get_by_label("First Name").fill(values.values["first_name"])
    await page.get_by_label("Last Name").fill(values.values["last_name"])
    await page.get_by_label("Email").fill(inbox.email_address)
    await page.get_by_label("Password").fill("12345Wasd")

async def click_create_account(page):
    await page.get_by_role("button", name="Create an account").click()