# requires install of schedule package
#pip3 install schedule

import schedule
from schedule import every , repeat # one is an annotation and other is a key word
import time as tm
from datetime import time, timedelta, datetime

#pass params by notation
#@repeat(every(5).seconds) would run job every 5 seconds
#@repeat(every(5).seconds, message="subscribe") adding a message, and would run job every 5 seconds
#@repeat(every(2).seconds, message="hey") would repeat both
def job():
    print("Sub to NeuralNine!")
# could pass message to job
#def job(message):
#   print("Hello the message is: ", message)

schedule.every().second.do(job) # every sec
schedule.every(5).seconds.do(job) # every 5 sec
schedule.every(5).to(10).seconds.do(job) # random 5 to 10 sec
schedule.every().second.do(job, message="helllooo") # us custom message in sched jobs

schedule.every().minute.do(job) # every min
schedule.every(5).minutes.do(job) # every 5 mins
schedule.every().minute.at(":40").do(job) # every min at 40 sec

schedule.every().hour.until(time(11, 33, 42)).do(job) # kinda confused on this time notaiton
schedule.every().hour.until(timedelta(hours=8)).do(job) # run for 8hrs then stop

schedule.every().day.at("10:30").do(job)
schedule.every().day.at("17:30").do(job)
schedule.every().monday.at("17:30").do(job)

j = schedule.every(1).to(5).seconds.do(job)
counter = 0
while True:
    schedule.run_pending()
    tm.sleep(1)

    # to show how to cancel job, cancels job not script
    counter += 1
    if counter == 10:
        schedule.cancel_job(j)