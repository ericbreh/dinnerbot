#dinnerbot account
username = 'dinnerbot50'
password = 'python1'

#for message to one person
message_to = 'ericchuang6' 
message = 'testing'

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys #for enter/tab key
from selenium.webdriver.common.action_chains import ActionChains #to just press enter
import schedule

def send_message_one_person():
    driver = webdriver.Chrome()
    actions = ActionChains(driver)
    
    driver.get("https://www.instagram.com/direct/new/")
    time.sleep(0.5)    

    user_box = driver.find_element(by=By.NAME, value="username")
    pass_box = driver.find_element(by=By.NAME, value="password")

    user_box.send_keys(username)
    pass_box.send_keys(password)
    pass_box.send_keys(Keys.ENTER)
    time.sleep(5)
   
    driver.find_element(By.XPATH, '//button[normalize-space()="Not Now"]').click()
    time.sleep(2)

    driver.find_element(By.XPATH, '//button[normalize-space()="Not Now"]').click()
    time.sleep(2)

    to_box = driver.find_element(By.NAME, 'queryBox')
    to_box.send_keys(message_to)
    time.sleep(2)
    to_box.send_keys(Keys.TAB)
    time.sleep(2)
    
    actions.send_keys(Keys.ENTER)
    actions.perform()
    time.sleep(2)

    driver.find_element(By.XPATH, '//button[normalize-space()="Next"]').click()
    time.sleep(5)

    actions.send_keys(message)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    time.sleep(2)

    driver.close()

#schedule.every().minute.do(send_message_one_person)

#while True:
#    schedule.run_pending()
#    time.sleep(1)
send_message_one_person()
