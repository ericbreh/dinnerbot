import schedule
import time


def thing():
    print('hi')
    

schedule.every(2).seconds.do(thing)

i = 0
while i <= 20:
    schedule.run_pending()
    time.sleep(1)
    i+=1