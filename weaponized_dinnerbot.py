# creates accounts
# i dont think it works 9/15/23

from playwright.sync_api import sync_playwright
import time
import multiprocessing

name = 'Cassidy'
password = 'fuckcassidy1!'


def create_account():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page1 = browser.new_page()
        page2 = browser.new_page()

        page1.goto("https://www.minuteinbox.com/")
        page2.goto("https://www.instagram.com/accounts/emailsignup/")

        email = page1.query_selector('#email').inner_text()

        page2.get_by_label('Mobile Number or Email').fill(email)
        page2.get_by_label('Username').click()
        time.sleep(1)
        page2.keyboard.press('Tab')
        page2.keyboard.press('Enter')
        page2.get_by_label('Full Name').fill(name)
        page2.get_by_label('Password').fill(password)
        page2.get_by_text('Sign up').nth(1).click()

        page2.get_by_title('Month:').click()
        for i in range(2):
            page2.keyboard.press('ArrowDown')
            i += 1
        page2.keyboard.press('Enter')

        page2.get_by_title('Day:').click()
        for i in range(4):
            page2.keyboard.press('ArrowDown')
            i += 1
        page2.keyboard.press('Enter')

        page2.get_by_title('Year:').click()
        for i in range(20):
            page2.keyboard.press('ArrowDown')
            i += 1
        page2.keyboard.press('Enter')

        page2.get_by_text('Next').nth(0).click()

        time.sleep(20)

        page1.reload()
        string = page1.query_selector('#schranka > tr:nth-child(1) > td:nth-child(2)').inner_text()
        code = string[:6]
        
        page2.get_by_role("textbox").fill(code)
        # page2.get_by_role("textbox").press('Enter')

        print(email)
        time.sleep(10)
        
def test():
     with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()
        page.goto("https://www.google.com/")
        time.sleep(20)


# if __name__ == '__main__':
#     num_processes = 10
#     processes = []
#     for i in range(num_processes):
#         p = multiprocessing.Process(target=test)
#         processes.append(p)
#         p.start()

#     for p in processes:
#         p.join()

create_account()