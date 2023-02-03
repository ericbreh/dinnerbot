#dinnerbot account
#username = 'dinnerbot50'
#password = 'python1'

#tamara account
username = 'hungry.tamara'
password = 'yourmomonmonday'

#for message to one person
message_to = 'ericchuang6' 
message = 'Dinner at 7'

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys #for enter/tab key
from selenium.webdriver.common.action_chains import ActionChains #to just press enter

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

def send_message_group():
    driver = webdriver.Chrome()
    actions = ActionChains(driver)
    
    driver.get("https://www.instagram.com/direct/inbox/")
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

    for i in range (13): #12 or 13 depending on in website has reels idk why
        actions.send_keys(Keys.TAB)
        actions.perform()

    actions.send_keys(Keys.ENTER)
    actions.perform()
    time.sleep(3)

    actions.send_keys(message)
    #actions.send_keys(Keys.ENTER)
    actions.perform()
    time.sleep(3)

    driver.close()


send_message_group()

#schedule.every().day.at("15:00").do(send_message_group)