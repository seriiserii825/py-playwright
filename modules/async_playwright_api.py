from playwright.async_api import async_playwright
import asyncio


def async_playwright_api():
    async def run():
        async with async_playwright() as p:
            # Launch the browser and create a new page
            browser = await p.chromium.launch(headless=False)
            page = await browser.new_page()
            await page.goto("https://iteco.altuofianco.com/")
            print(await page.title())
            await page.screenshot(path="screenshot.png")
            await browser.close()

    asyncio.run(run())
