from playwright.sync_api import sync_playwright


def locators():
    with sync_playwright() as p:
        # Launch the browser and create a new page
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://iteco.altuofianco.com/")
        button = page.locator('.about__btn .btn')
        # Wait for the button to be visible
        button.wait_for(state="visible", timeout=2000)
        print(f"Button text: {button.inner_text()}")
        # Wait for 2 seconds before taking the screenshot
        page.screenshot(path="button_screenshot.png")
        button.click()
        input("Press Enter to close...")
        browser.close()
