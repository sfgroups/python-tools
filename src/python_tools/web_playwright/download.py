import io
import time
from pathlib import Path

import requests
from PIL import Image
from playwright.sync_api import Playwright

from python_tools.utils.captcha2text import resolve_captcha

work_dir = Path(Path.home(), 'work', 'playwright')


def solve_captcha(page, base_url):
    # Get the captcha image element
    captcha_element = page.query_selector("#captcha")
    page.get_by_role("img", name="Captcha").click()
    img_lst = []
    # Get the image source URL
    captcha_url = captcha_element.get_attribute("src")
    captcha_image_url = ""
    all_links = page.query_selector_all('img')
    for link in all_links:
        if "SimpleCaptcha" in link.get_attribute("src"):
            print(link)
            captcha_image_url = base_url + link.get_attribute('src')
            break

    response = requests.get(captcha_image_url).content
    image_file = io.BytesIO(response)
    image = Image.open(image_file)
    download_file = f"{work_dir}/captcha.png"
    with open(download_file, "wb") as f:
        image.save(f, "PNG")

    # Process the captcha image (e.g. using a third-party OCR library)
    # captcha_text = solve_captcha_image(captcha_image_path)
    #
    # # Enter the captcha text in the input field
    # captcha_input_element = await page.query_selector("#captcha-input")
    # await captcha_input_element.type(captcha_text)


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://tnreginet.gov.in/portal/index.jsp")
    page.wait_for_selector("#cmnCaptchDivId")

    solve_captcha(page, "https://tnreginet.gov.in/portal/")
    print("Waiting for 20 seconds")
    time.sleep(20)
    # page.get_by_label("பயனர் பெயர்").click()
    # page.get_by_label("பயனர் பெயர்").fill("username")
    # page.get_by_label("பயனர் பெயர்").press("Tab")
    # page.get_by_label("கடவுச்சொல்").fill("password")
    # page.get_by_label("கடவுச்சொல்").press("Tab")
    # page.get_by_label("காண்பிக்கப்படும் குறியீட்டைத் தட்டச்சு செய்க").press("CapsLock")
    # page.get_by_label("காண்பிக்கப்படும் குறியீட்டைத் தட்டச்சு செய்க").fill("8XH58")
    # page.get_by_role("button", name="உள்நுழைவு").click()
    # page.wait_for_url("https://tnreginet.gov.in/portal/index.jsp")
    # ---------------------
    context.close()
    browser.close()


if __name__ == '__main__':
    for f in ["SimpleCaptcha.png", "captcha.png", "SimpleCaptcha1.png"]:
        download_file = f"{work_dir}/{f}"
        print(download_file)
        text = resolve_captcha(download_file)
        print(f"First: [{text}]")

    # with sync_playwright() as playwright:
    #     run(playwright)
