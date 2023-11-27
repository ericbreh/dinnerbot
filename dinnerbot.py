from playwright.sync_api import sync_playwright
import schedule
import time
import random
from datetime import datetime

username = 'dinnerbot50'
password = 'python1'
message_to = 'Order of the cone'


def send_dinner_message():

    # set random time
    minute = random.randrange(0,60)
    hour_range = random.randrange(100)
    hour = 7
    if hour_range in range(0,45):
        hour = 6
    if hour_range in range(45,90):
        hour = 7
    if hour_range in range(90,95):
        hour = 5
    if hour_range in range(95,100):
        hour = 8


    if datetime.today().weekday() <= 3: # monday-thursday
        # set random dh for monday-thursday
        if hour == 8:
            dh_range = random.randrange(60,100)
        elif hour == 7 and minute > 20:
            dh_range = random.randrange(60,100)
        else:
            dh_range = random.randrange(100)

        dining_hall = ''
        if dh_range in range(1,60):
            dining_hall = 'Merrill'
        if dh_range in range(60,80):
            dining_hall = 'Cowell'
        if dh_range in range(80,100):
            dining_hall = '9/10'
        if dh_range == 0:
            dining_hall = 'Porter'


    if datetime.today().weekday() == 4: # friday
        # set random dh for friday
        if hour == 8:
            dh_range = random.randrange(80,100)
        elif hour == 7 and minute > 20:
            dh_range = random.randrange(80,100)
        else:
            dh_range = random.randrange(100)

        dining_hall = ''
        if dh_range in range(1,60):
            dining_hall = 'Merrill'
        if dh_range in range(60,80):
            dining_hall = 'Cowell'
        if dh_range in range(80,100):
            dining_hall = '9/10'
        if dh_range == 0:
            dining_hall = 'Porter'
    

    if datetime.today().weekday() == 5: # saturday
        # set random dh for saturday
        if hour == 8:
            dh_range = random.randrange(50,100)
        elif hour == 7 and minute > 20:
            dh_range = random.randrange(50,100)
        else:
            dh_range = random.randrange(90)

        dining_hall = ''
        if dh_range in range(1,50):
            dining_hall = 'Cowell'
        if dh_range in range(50,100):
            dining_hall = '9/10'
        if dh_range == 0:
            dining_hall = 'Porter'


    if datetime.today().weekday() == 6: # sunday
        # set random dh for sunday
        dh_range = random.randrange(100)

        dining_hall = ''
        if dh_range in range(1,50):
            dining_hall = 'Cowell'
        if dh_range in range(50,100):
            dining_hall = '9/10'
        if dh_range == 0:
            dining_hall = 'Porter'

    
    dinner_message = f'Dinner at {dining_hall} at {hour}:{str(minute).zfill(2)} pm'

    # send the dinner_message
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.instagram.com/direct/inbox/")
        page.get_by_label('username').fill(username)
        page.get_by_label('password').fill(password)
        page.get_by_text('Log in').nth(0).click()
        page.get_by_text('Not Now').nth(0).click()
        page.get_by_text(message_to).nth(0).click()
        page.get_by_role("textbox").fill(dinner_message)
        page.get_by_role("textbox").press('Enter')

    

schedule.every().day.at("15:00").do(send_dinner_message)
while True:
    schedule.run_pending()
    time.sleep(1)
