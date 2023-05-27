import time
from pathlib import Path

from dotenv import find_dotenv, dotenv_values
from playwright.sync_api import Playwright
from playwright.sync_api import sync_playwright
from requests.structures import CaseInsensitiveDict

from python_tools.utils.captcha2text import resolve_captcha

work_dir = Path(Path.home(), 'work', 'playwright')


def download_patta(page) -> None:
    config = CaseInsensitiveDict(dotenv_values(find_dotenv()))

    dc = config['DISTRICT_CODE']
    tc = config['TALUK_CODE']
    vc = config['VILLAGE_CODE']
    web_url = config['TN_URL']

    patta_no = "623"
    page.goto(web_url, wait_until="load")
    page.locator("select[name=\"districtCode\"]").select_option(dc)
    page.locator("select[name=\"talukCode\"]").select_option(tc)
    page.locator("select[name=\"villageCode\"]").select_option(vc)
    page.locator("input[name=\"viewOpt\"]").first.check()

    page.locator("input[name=\"pattaNo\"]").click()
    page.locator("input[name=\"pattaNo\"]").fill(patta_no)

    page.locator("input[name=\"captcha\"]").click()
    page.locator("input[name=\"captcha\"]").press("CapsLock")

    download_file = f"{work_dir}/screenshot.png"
    page.locator("#captcha_name").screenshot(path=download_file)
    text = resolve_captcha(download_file)
    print(f"captcha: [{text}]")

    page.locator("input[name=\"captcha\"]").fill(text)
    time.sleep(3)
    page.get_by_role("button", name="சமர்ப்பி").click()
    time.sleep(3)
    page.emulate_media(media="print")
    pdf_file = f"{work_dir}/{patta_no}.pdf"
    page.pdf(path=pdf_file)

    # Get the page's HTML content
    html_content = page.content()
    html_file = pdf_file.replace('.pdf', '.html')
    # Save the HTML content to a file
    with open(html_file, 'w') as f:
        f.write(html_content)


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    download_patta(page)

    context.close()
    browser.close()


if __name__ == '__main__':
    with sync_playwright() as playwright:
        run(playwright)
