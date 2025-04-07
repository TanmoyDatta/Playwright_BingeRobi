import asyncio
from playwright.async_api import async_playwright

async def main():
   async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://binge.buzz")
        print('chrome successfully Opened')
        print(await page.title())
        await page.wait_for_timeout(5000)
    

        await page.screenshot(path="homepage.png")
        await browser.close()
    
asyncio.run(main())