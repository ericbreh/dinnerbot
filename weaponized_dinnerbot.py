from playwright.sync_api import sync_playwright
import time

def create_account():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.minuteinbox.com/")
        page.get_by_text('Copy').nth(0).click()
        
        

        time.sleep(5)
        

create_account()