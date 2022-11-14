from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()

    page.goto("https://eservices.tn.gov.in/eservicesnew/home.html")

    page.get_by_role("link", name="பட்டா / சிட்டா விவரங்களை பார்வையிட").click()
    page.wait_for_url("https://eservices.tn.gov.in/eservicesnew/land/chittaNewRuralTamil.html?lan=ta")

    page.locator("select[name=\"districtCode\"]").select_option("08")

    page.locator("select[name=\"talukCode\"]").select_option("04")

    page.locator("select[name=\"villageCode\"]").select_option("055")

    page.locator("input[name=\"viewOpt\"]").first.check()

    page.locator("input[name=\"pattaNo\"]").click()

    page.locator("input[name=\"pattaNo\"]").fill("183")

    page.locator("input[name=\"captcha\"]").click()

    page.locator("input[name=\"captcha\"]").fill("55WRWv")

    page.get_by_role("button", name="சமர்ப்பி").click()
    page.wait_for_url("https://eservices.tn.gov.in/eservicesnew/land/chittaExtract_ta.html?lan=ta")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
