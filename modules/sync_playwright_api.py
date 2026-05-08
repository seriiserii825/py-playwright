from playwright.sync_api import sync_playwright


def sync_playwright_api():
    with sync_playwright() as p:
        # Launch the browser and create a new page
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://iteco.altuofianco.com/")
        print(page.title())
        page.screenshot(path="screenshot.png")
        browser.close()
