from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Go to the Binge Buzz homepage
        page.goto("https://binge.buzz/")

        # Login with email
        page.get_by_role("button", name="Login").click()
        page.get_by_role("button", name="Login with Email").click()
        page.get_by_role("textbox", name="Enter Email to Sign-in").fill("mrtanmoy64@gmail.com")
        page.get_by_role("textbox", name="Enter password").click()
        page.get_by_role("textbox", name="Enter password").fill("Test1234#")
        page.get_by_test_id("SearchIcon").click()
        time.sleep(3)
        page.get_by_role("button", name="Submit").click()
        # Search for a show/movie
        page.get_by_role("combobox", name="Search Shows and Movies...").click()
        page.get_by_role("combobox", name="Search Shows and Movies...").fill("The waking of")
        page.get_by_role("option", name="The Waking of a Nation").first.click()

        # Click on the first movie card
        page.locator(".BingePaper-root > img").first.click()

        # Open more info
        page.get_by_role("button", name="More Info").click()

        # Click the second unnamed button (possibly close or play)
        page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(1).click()

        # Return to Binge Home
        page.get_by_role("button", name="Binge Home").click()

        page.wait_for_timeout(5000)
        browser.close()

run()
