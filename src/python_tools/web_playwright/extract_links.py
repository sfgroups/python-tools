import asyncio
from playwright.async_api import async_playwright, Error

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()

        # Navigate to the website to be scraped
        await page.goto('https://www.sfgroups.com/')

        # Extract the title of the webpage
        title = await page.title()
        print(f'Title of the webpage: {title}')

        # Extract all the links in the webpage
        links = await page.query_selector_all('a')
        for link in links:
            href = await link.get_attribute('href')
            print(href)

        # Close the browser and context
        await context.close()
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
