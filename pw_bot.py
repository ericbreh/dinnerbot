#dinnerbot account
username = 'dinnerbot50'
password = 'python1'
message_to = 'Order of the cone'
message = 'WAKE UP BOSEPH'

from playwright.sync_api import sync_playwright
import time

def send_message():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.instagram.com/direct/inbox/")

        page.get_by_label('username').fill(username)
        page.get_by_label('password').fill(password)
        page.get_by_text('Log in').nth(0).click()
        page.get_by_text('Not Now').nth(0).click()
        #page.get_by_text('Not Now').nth(0).click() #headless false
        page.get_by_text(message_to).nth(0).click()
        for i in range(50):
            page.get_by_role("textbox").fill(message)
            page.get_by_role("textbox").press('Enter')

            
        # time.sleep(5)
        # page.screenshot(path="1.png")


send_message()