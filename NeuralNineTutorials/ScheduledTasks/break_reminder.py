# requires install of schedule package
#pip3 install schedule

import schedule
from schedule import every , repeat # one is an annotation and other is a key word
import time as tm
from datetime import time, timedelta, datetime

# commented parts are only needed for this without the schedule.every, with/without the while loop
#@repeat(every(30).minutes) # one way as notation
#def break_reminder():
#    print("Take a break! You have been working for 30 minutes!")

def break_reminder():
    print("Take a break! You have been working for 30 minutes!")

schedule.every().day.at("10:00").do(break_reminder)

while True:
    schedule.run_pending()
    tm.sleep(1)