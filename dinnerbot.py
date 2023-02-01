username = 'hungry.tamara'
password = 'yourmomonmonday'
message_to = 'honey nut cheerios'
message = 'Dinner at 7'

from playwright.sync_api import sync_playwright
import schedule
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
        page.get_by_text(message_to).nth(0).click()
        page.get_by_role("textbox").fill(message)
        page.get_by_role("textbox").press('Enter')

schedule.every().day.at("15:00").do(send_message)
while True:
    schedule.run_pending()
    time.sleep(1)