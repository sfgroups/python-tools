from pathlib import Path

from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
    browser = playwright.chromium.launch()
    page = browser.new_page()

    html_file_path = '/Users/sundaram/work/sample.html'
    with open(html_file_path, 'r') as html_file:
        html_content = html_file.read()
    page.set_content(html_content)

    page.wait_for_load_state('networkidle')

    p = Path(html_file_path ).parent
    s = f"{Path(html_file_path ).stem}.pdf"
    pdf_file_path = str(Path(p,s ))
    print(pdf_file_path)
    pdf_options = {
        'path': pdf_file_path,
        'format': 'a4',
    }
    page.pdf(path=pdf_file_path)

    page.close()
    browser.close()


with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.sfgroups.com")

    page.screenshot(path=f"{Path(html_file_path ).parent}/example.png")
    page.close()
    browser.close()
