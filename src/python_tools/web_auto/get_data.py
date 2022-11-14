from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()

    page.goto("https://playwright.dev/")

    page.get_by_role("link", name="Get started").click()
    page.wait_for_url("https://playwright.dev/docs/intro")

    page.get_by_role("link", name="API testing").click()
    page.wait_for_url("https://playwright.dev/docs/test-api-testing")

    page.get_by_role("tab", name="JavaScript").nth(2).click()

    page.locator("li:has-text(\"associated with a BrowserContext\")").get_by_role("link", name="BrowserContext").click()
    page.wait_for_url("https://playwright.dev/docs/api/class-browsercontext")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
