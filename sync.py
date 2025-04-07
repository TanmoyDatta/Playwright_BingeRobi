from playwright.sync_api import sync_playwright
import time
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    page.goto("https://binge.buzz")
    print('Chrome successfully opened')
    print(page.title())
    page.wait_for_timeout(2000)
    page.screenshot(path="demo.png")
    
    # scroll view
    page.mouse.wheel(0,2000)
    time.sleep(2)
    
    page.click('#root > header > div > div.BingeBox-root.css-gi3fs5 > button')
    # login = page.wait_for_selector('#root > header > div > div.BingeBox-root.css-gi3fs5 > button')
    # login.click()
    
    # Login with Google
    page.click("//button[@aria-label='Login with Google']")
    
    # phoneNum = page.wait_for_selector('input[placeholder="Enter phone number"]')
    # phoneNum.type('01833183992')
    
    # G_OTP = page.wait_for_selector('.BingeBtnBase-root.css-1h228gw')
    # G_OTP.click()
    page.wait_for_timeout(2000)
    
    popup = context.wait_for_event("page")
    popup.wait_for_load_state()

    # Step 4: Enter email
    popup.fill("//input[@id='identifierId']", mrtanmoy64@gmail.com)
    popup.click("//span[normalize-space()='Next']")
    
    # gmail=page.wait_for_selector("//input[@id='identifierId']")
    # gmail.type('mrtanmoy64@gmail.com')
    # page.click("//span[normalize-space()='Next']")
    
