from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com")
    locator = page.locator('login-button').click
    page.screenshot(path="demo.png")
    page.wait_for_timeout(500)
    browser.close()