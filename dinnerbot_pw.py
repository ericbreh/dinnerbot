#dinnerbot account
username = 'dinnerbot50'
password = 'python1'
message_to = 'Eric Chuang'
message = 'Dinner at 7'

from playwright.sync_api import sync_playwright, ViewportSize
import time

def send_message():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.set_viewport_size(ViewportSize(width = 1000*2, height = 1920*2))
        page.goto("https://www.instagram.com/direct/inbox/")

        page.get_by_label('username').fill(username)
        page.get_by_label('password').fill(password)
        page.get_by_text('Log in').nth(0).click()
        page.get_by_text('Not Now').nth(0).click()
        time.sleep(4)
        page.get_by_text('Not Now').nth(0).click()
        page.get_by_text(message_to).nth(0).click()
        page.get_by_role("textbox").fill(message)
        page.get_by_role("textbox").press('Enter')


send_message()