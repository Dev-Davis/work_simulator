import time

import timeclock
import sys

print("""
/////////////////
Welcome to *Work*
/////////////////
""")
time.sleep(0.7)
print('Clock in? y/n: \n')
# print('1. Clock In')
# print('2. Start Lunch')
# print('3. End Lunch')
# print('4. Clock Out')

user_punch = input('Select an option: \n')

match user_punch:
    case 'y':
        timeclock.work()
    case 'n':
        print("You aren't clocked in")
